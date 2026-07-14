from sqlalchemy import Column, Integer, String

from . import Base


class Proveedor(Base):
    __tablename__ = "proveedores"

    id_proveedor = Column(Integer, primary_key=True)
    nombre_proveedor = Column(String(150), nullable=False, unique=True, index=True)
    contacto_email = Column(String(150))
    telefono = Column(String(20))