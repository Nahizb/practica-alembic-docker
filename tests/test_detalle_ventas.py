import pytest
from app.models.detalle_ventas import DetalleVenta
from app.models.ventas import Venta
from app.models.productos import Producto
from app.models.clientes import Cliente

def test_insert_detalle_venta(db):
    # Crear cliente
    cliente = Cliente(nombre_cliente="Test", dni_cliente="0000X", telefono="600000000")
    db.add(cliente)
    db.flush()

    # Crear producto
    producto = Producto(
        nombre_producto="ProdTest",
        precio_unitario=10.00,
        categoria="Test",
        stock=50
    )
    db.add(producto)
    db.flush()

    # Crear venta
    venta = Venta(id_cliente=cliente.id_cliente)
    db.add(venta)
    db.flush()

    # Crear detalle
    detalle = DetalleVenta(
        id_venta=venta.id_venta,
        id_producto=producto.id_producto,
        cantidad=3,
        precio_unitario=producto.precio_unitario
    )
    db.add(detalle)
    db.flush()

    # Verificar
    d = db.query(DetalleVenta).filter_by(id_detalle=detalle.id_detalle).first()

    assert d is not None
    assert d.cantidad == 3
    assert d.precio_unitario == producto.precio_unitario
    assert d.venta.id_venta == venta.id_venta
    assert d.producto.id_producto == producto.id_producto
