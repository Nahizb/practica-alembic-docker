import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command

TEST_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:5432@db:5432/postgres_test"  # default para uso local dentro del contenedor app
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


def _alembic_config() -> Config:
    """Construye la config de Alembic apuntando a la DB de test."""
    cfg = Config(os.path.join(ROOT_DIR, "alembic.ini"))
    cfg.set_main_option("script_location", os.path.join(ROOT_DIR, "alembic"))
    # env.py lee DATABASE_URL desde el entorno (os.getenv), así que
    # sobreescribimos la variable de entorno ANTES de que env.py la lea.
    os.environ["DATABASE_URL"] = TEST_DATABASE_URL
    return cfg


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    cfg = _alembic_config()
    # Empezamos desde un estado completamente limpio
    command.downgrade(cfg, "base")
    # Corre TODAS las migraciones reales, en orden, tal como en producción
    command.upgrade(cfg, "head")
    yield
    command.downgrade(cfg, "base")


@pytest.fixture
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()