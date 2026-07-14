from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from . import Base


class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True)
    nombre_producto = Column(String(100), nullable=False, index=True)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    categoria = Column(String(50), index=True)
    stock = Column(Integer, nullable=False, server_default='0')

    detalles = relationship("DetalleVenta", back_populates="producto")