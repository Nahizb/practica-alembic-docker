"""agregar telefono a clientes

Revision ID: f2e8eb2a5a88
Revises: afffd9a2ec7c
Create Date: 2026-07-15 11:17:33.756360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f2e8eb2a5a88'
down_revision: Union[str, None] = 'afffd9a2ec7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.drop_column('clientes', 'elefono')
    op.add_column('clientes', sa.Column('telefono', sa.String(length=20), nullable=True))


def downgrade() -> None:
    op.drop_column('clientes', 'telefono')
    op.add_column('clientes', sa.Column('elefono', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###
