import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command

# IMPORTANTE: usamos un nombre de variable DISTINTO a DATABASE_URL
# a propósito, para que nunca pueda colisionar con la variable real
# que usa la aplicación (definida en .env / docker-compose env_file).
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql://postgres:5432@db:5432/postgres_test"
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


def _assert_is_test_database(url: str) -> None:
    """Salvaguarda: nunca permitir downgrade/upgrade destructivo
    si la URL no apunta claramente a una base de datos de test."""
    if "test" not in url.lower():
        raise RuntimeError(
            f"BLOQUEADO: '{url}' no parece una base de datos de TEST "
            "(no contiene 'test' en el nombre). Abortando para evitar "
            "borrar datos reales por accidente."
        )


def _alembic_config() -> Config:
    _assert_is_test_database(TEST_DATABASE_URL)
    cfg = Config(os.path.join(ROOT_DIR, "alembic.ini"))
    cfg.set_main_option("script_location", os.path.join(ROOT_DIR, "alembic"))
    os.environ["DATABASE_URL"] = TEST_DATABASE_URL
    return cfg


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    cfg = _alembic_config()
    command.downgrade(cfg, "base")
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