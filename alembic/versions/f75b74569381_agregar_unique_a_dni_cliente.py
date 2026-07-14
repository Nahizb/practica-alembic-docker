"""agregar unique a dni_cliente

Revision ID: f75b74569381
Revises: 77accdf32ec1
Create Date: 2026-07-09 12:37:18.734278

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f75b74569381'
down_revision: Union[str, None] = '77accdf32ec1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint('clientes_dni_cliente_key', 'clientes', ['dni_cliente'])


def downgrade() -> None:
    op.drop_constraint('clientes_dni_cliente_key', 'clientes', type_='unique')