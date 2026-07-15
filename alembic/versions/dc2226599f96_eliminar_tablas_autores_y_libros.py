"""eliminar tablas autores y libros

Revision ID: dc2226599f96
Revises: f2e8eb2a5a88
Create Date: 2026-07-15 11:43:24.921288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc2226599f96'
down_revision: Union[str, None] = 'f2e8eb2a5a88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('libros')
    op.drop_table('autores')


def downgrade() -> None:
    op.create_table(
        'autores',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('nacionalidad', sa.String(length=50)),
    )
    op.create_table(
        'libros',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('titulo', sa.String(length=200), nullable=False),
        sa.Column('anio_publicacion', sa.Integer()),
        sa.Column('autor_id', sa.Integer(), sa.ForeignKey('autores.id')),
        sa.Column('creado_en', sa.DateTime()),
    )