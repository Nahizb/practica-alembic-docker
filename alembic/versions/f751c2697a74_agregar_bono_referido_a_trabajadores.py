"""agregar bono referido a trabajadores

Revision ID: f751c2697a74
Revises: f7a86de0f401
Create Date: 2026-07-17 15:16:50.168228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f751c2697a74'
down_revision: Union[str, None] = 'f7a86de0f401'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'trabajadores',
        sa.Column('bono_referido', sa.Numeric(10, 2), nullable=True, server_default='0'),
    )

    # Bono fijo mensual del programa de referidos, repartido entre la planilla actual.
    # Si todavia no hay trabajadores (p. ej. una base recien creada) no hay nada que repartir,
    # y el server_default deja a los futuros inserts en 0 en vez de romper por NOT NULL.
    op.execute("""
        DO $$
        DECLARE
            total_trabajadores INTEGER;
        BEGIN
            SELECT COUNT(*) INTO total_trabajadores FROM trabajadores;

            IF total_trabajadores > 0 THEN
                UPDATE trabajadores
                SET bono_referido = 5000.00 / total_trabajadores;
            END IF;
        END $$;
    """)

    op.alter_column('trabajadores', 'bono_referido', nullable=False)


def downgrade() -> None:
    op.drop_column('trabajadores', 'bono_referido')
