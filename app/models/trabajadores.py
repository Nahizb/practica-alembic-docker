from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Trabajador(Base):
    __tablename__ = "trabajadores"

    id_trabajador = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    id_puesto = Column(Integer, ForeignKey("puestos.id_puesto"), nullable=False)
    email = Column(String(45), nullable=False)

    puesto = relationship("Puesto", back_populates="trabajadores")
    departamentos = relationship("TrabajadorDepartamento", back_populates="trabajador")

