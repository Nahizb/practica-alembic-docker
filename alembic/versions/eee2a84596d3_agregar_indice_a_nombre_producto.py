"""agregar indice a nombre_producto

Revision ID: eee2a84596d3
Revises: 5d8adb70ef6a
Create Date: 2026-07-10 19:25:44.720009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eee2a84596d3'
down_revision: Union[str, None] = '5d8adb70ef6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # ❌ NO usar drop_index
    # ❌ NO usar create_index normal

    with op.get_context().autocommit_block():
        op.execute(
            "DROP INDEX IF EXISTS ix_productos_nombre;"
        )
        op.execute(
            "CREATE INDEX CONCURRENTLY ix_productos_nombre_producto "
            "ON productos(nombre_producto);"
        )

def downgrade():
    with op.get_context().autocommit_block():
        op.execute(
            "DROP INDEX CONCURRENTLY ix_productos_nombre_producto;"
        )
