"""crear tabla trabajador_departamento nm

Revision ID: 38d3c6f63ada
Revises: f7a86de0f401
Create Date: 2026-07-17 17:00:29.162962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38d3c6f63ada'
down_revision: Union[str, None] = 'f7a86de0f401'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "trabajador_departamento",
        sa.Column("id_asignacion", sa.Integer(), primary_key=True),
        sa.Column("id_trabajador", sa.Integer(), sa.ForeignKey("trabajadores.id_trabajador"), nullable=False),
        sa.Column("id_departamento", sa.Integer(), sa.ForeignKey("departamentos.id_departamento"), nullable=False),
        sa.Column("rol", sa.String(50), nullable=True),
        sa.Column("fecha_asignacion", sa.Date(), nullable=False, server_default=sa.func.current_date()),
        sa.UniqueConstraint(
            "id_trabajador", "id_departamento", "fecha_asignacion",
            name="uq_trabajador_departamento_fecha",
        ),
    )
    op.create_index("ix_trabajador_departamento_id_trabajador", "trabajador_departamento", ["id_trabajador"])
    op.create_index("ix_trabajador_departamento_id_departamento", "trabajador_departamento", ["id_departamento"])


def downgrade() -> None:
    op.drop_index("ix_trabajador_departamento_id_departamento", table_name="trabajador_departamento")
    op.drop_index("ix_trabajador_departamento_id_trabajador", table_name="trabajador_departamento")
    op.drop_table("trabajador_departamento")