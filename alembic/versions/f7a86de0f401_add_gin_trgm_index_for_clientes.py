"""add gin trgm index for clientes

Revision ID: f7a86de0f401
Revises: f55c34ca5dfc
Create Date: 2026-07-16 12:52:23.816332

"""
from alembic import op
import sqlalchemy as sa

revision = 'f7a86de0f401'
down_revision = 'f55c34ca5dfc'
branch_labels = None
depends_on = None

transaction_per_migration = True

def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")

    op.create_index(
        'idx_clientes_nombre_trgm',
        'clientes',
        ['nombre_cliente'],
        postgresql_using='gin',
        postgresql_ops={'nombre_cliente': 'gin_trgm_ops'},
        postgresql_concurrently=True
    )

def downgrade():
    op.drop_index('idx_clientes_nombre_trgm', table_name='clientes')
