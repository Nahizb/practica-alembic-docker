"""agregar indice a categoria

Revision ID: 5d8adb70ef6a
Revises: 7b704a24b23a
Create Date: 2026-07-10 13:02:32.275585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d8adb70ef6a'
down_revision: Union[str, None] = '7b704a24b23a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_index('ix_productos_categoria', 'productos', ['categoria'])


def downgrade() -> None:
    op.drop_index('ix_productos_categoria', table_name='productos')