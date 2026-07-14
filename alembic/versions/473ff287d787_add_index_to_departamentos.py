"""add index to departamentos

Revision ID: 473ff287d787
Revises: 7edc9946ec1d
Create Date: 2026-07-13 18:49:39.586105
"""

from typing import Sequence, Union
from alembic import op
from alembic import context

# revision identifiers, used by Alembic.
revision: str = '473ff287d787'
down_revision: Union[str, None] = '7edc9946ec1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    with op.get_context().autocommit_block():
        op.execute(
            "CREATE INDEX CONCURRENTLY idx_departamento_nombre "
            "ON departamentos(nombre_departamento);"
        )

def downgrade():
    with op.get_context().autocommit_block():
        op.execute(
            "DROP INDEX CONCURRENTLY idx_departamento_nombre;"
        )