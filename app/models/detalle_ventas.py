from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from . import Base


class DetalleVenta(Base):
    __tablename__ = "detalle_ventas"

    id_detalle = Column(Integer, primary_key=True)
    id_venta = Column(Integer, ForeignKey("ventas.id_venta"), nullable=False)
    id_producto = Column(Integer, ForeignKey("productos.id_producto"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)

    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles")