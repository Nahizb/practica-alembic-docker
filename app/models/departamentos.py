from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Departamento(Base):
    __tablename__ = "departamentos"
    id_departamento = Column(Integer, primary_key=True)
    nombre_departamento = Column(String(50), nullable=False, unique=True, index=True)
    descripcion = Column(String(200))

    trabajadores = relationship("TrabajadorDepartamento", back_populates="departamento")