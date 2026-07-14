"""unir stock y categoria

Revision ID: 7b704a24b23a
Revises: 2c229a6f1c99, 9bb05211070e
Create Date: 2026-07-10 12:32:42.837486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b704a24b23a'
down_revision: Union[str, None] = ('2c229a6f1c99', '9bb05211070e')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
