from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from . import Base


class TrabajadorDepartamento(Base):
    __tablename__ = "trabajador_departamento"

    id_asignacion = Column(Integer, primary_key=True)
    id_trabajador = Column(Integer, ForeignKey("trabajadores.id_trabajador"), nullable=False, index=True)
    id_departamento = Column(Integer, ForeignKey("departamentos.id_departamento"), nullable=False, index=True)
    rol = Column(String(50), nullable=True)  # rol del trabajador dentro de ese departamento
    fecha_asignacion = Column(Date, nullable=False, server_default=func.current_date())

    trabajador = relationship("Trabajador", back_populates="departamentos")
    departamento = relationship("Departamento", back_populates="trabajadores")

    __table_args__ = (
        UniqueConstraint(
            "id_trabajador", "id_departamento", "fecha_asignacion",
            name="uq_trabajador_departamento_fecha",
        ),
    )