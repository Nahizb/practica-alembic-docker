"""agregar categoria a productos

Revision ID: 9bb05211070e
Revises: 64bd56eb4166
Create Date: 2026-07-10 12:25:45.582049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bb05211070e'
down_revision: Union[str, None] = '64bd56eb4166'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('productos', sa.Column('categoria', sa.String(length=50), nullable=True))


def downgrade() -> None:
    op.drop_column('productos', 'categoria')