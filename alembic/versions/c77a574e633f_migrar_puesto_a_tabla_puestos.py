"""migrar puesto a tabla puestos

Revision ID: c77a574e633f
Revises: f75b74569381
Create Date: 2026-07-09 13:35:11.598011

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c77a574e633f'
down_revision: Union[str, None] = 'f75b74569381'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Crear la tabla nueva "puestos"
    op.create_table(
        'puestos',
        sa.Column('id_puesto', sa.Integer(), primary_key=True),
        sa.Column('nombre_puesto', sa.String(length=45), nullable=False, unique=True),
    )

    # 2. Poblarla con los valores distintos que ya existen en trabajadores.puesto
    op.execute("INSERT INTO puestos (nombre_puesto) VALUES ('Cajero')")
    op.execute("INSERT INTO puestos (nombre_puesto) VALUES ('Supervisora')")
    op.execute("INSERT INTO puestos (nombre_puesto) VALUES ('Vendedor')")
    op.execute("INSERT INTO puestos (nombre_puesto) VALUES ('Gerente')")

    # 3. Agregar la columna nueva a trabajadores, opcional por ahora
    op.add_column('trabajadores', sa.Column('id_puesto', sa.Integer(), nullable=True))

    # 4. Rellenar id_puesto cruzando el texto viejo contra la tabla nueva
    op.execute("""
        UPDATE trabajadores
        SET id_puesto = puestos.id_puesto
        FROM puestos
        WHERE trabajadores.puesto = puestos.nombre_puesto
    """)

    # 5. Volverla obligatoria y agregar la Foreign Key
    op.alter_column('trabajadores', 'id_puesto', nullable=False)
    op.create_foreign_key(
        'fk_trabajadores_puesto', 'trabajadores', 'puestos',
        ['id_puesto'], ['id_puesto']
    )

    # 6. Eliminar la columna vieja de texto libre
    op.drop_column('trabajadores', 'puesto')


def downgrade() -> None:
    # Reversa exacta, en orden contrario

    # 6 -> Restaurar la columna de texto libre
    op.add_column('trabajadores', sa.Column('puesto', sa.String(length=45), nullable=True))

    # 5 -> Quitar la FK antes de poder tocar la columna
    op.drop_constraint('fk_trabajadores_puesto', 'trabajadores', type_='foreignkey')

    # 4 -> Rellenar puesto (texto) a partir de id_puesto
    op.execute("""
        UPDATE trabajadores
        SET puesto = puestos.nombre_puesto
        FROM puestos
        WHERE trabajadores.id_puesto = puestos.id_puesto
    """)

    # 3 -> Volver puesto obligatoria, ya con datos
    op.alter_column('trabajadores', 'puesto', nullable=False)

    # Quitar la columna nueva
    op.drop_column('trabajadores', 'id_puesto')

    # 1 -> Eliminar la tabla puestos
    op.drop_table('puestos')