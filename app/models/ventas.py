from sqlalchemy import Column, Integer,  ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Venta(Base):
    __tablename__ = "ventas"

    id_venta = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    detalles = relationship("DetalleVenta", back_populates="venta")
