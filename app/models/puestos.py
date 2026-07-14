from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Puesto(Base):
    __tablename__ = "puestos"

    id_puesto = Column(Integer, primary_key=True)
    nombre_puesto = Column(String(45), nullable=False, unique=True)

    trabajadores = relationship("Trabajador", back_populates="puesto")