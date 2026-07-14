from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nombre_cliente = Column(String(45), nullable=False)
    dni_cliente = Column(String(12), nullable=False, unique=True)
    telefono = Column(String(20))  # ← Nuevo campo prueba githubactions