"""add indexes for ventas and detalle_ventas

Revision ID: f55c34ca5dfc
Revises: 086db39fcb1b
Create Date: 2026-07-16 12:36:06.627803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f55c34ca5dfc'
down_revision: Union[str, None] = '086db39fcb1b'
transaction_per_migration = True
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_index(
        'idx_detalle_ventas_venta',
        'detalle_ventas',
        ['id_venta', 'id_producto'],
        postgresql_concurrently=True
    )

    op.create_index(
        'idx_ventas_cliente',
        'ventas',
        ['id_cliente', 'id_venta'],
        postgresql_concurrently=True
    )

    op.create_index(
        'idx_detalle_ventas_producto',
        'detalle_ventas',
        ['id_producto', 'id_venta'],
        postgresql_concurrently=True
    )

def downgrade():
    op.drop_index('idx_detalle_ventas_venta', table_name='detalle_ventas')
    op.drop_index('idx_ventas_cliente', table_name='ventas')
    op.drop_index('idx_detalle_ventas_producto', table_name='detalle_ventas')
