"""agregar stock a productos

Revision ID: 2c229a6f1c99
Revises: 64bd56eb4166
Create Date: 2026-07-10 12:20:39.882324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c229a6f1c99'
down_revision: Union[str, None] = '64bd56eb4166'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('productos', sa.Column('stock', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('productos', 'stock')