from app.models.clientes import Cliente
from app.models.ventas import Venta

def test_crear_venta(db):
    cliente = Cliente(nombre_cliente="Juan", dni_cliente="XYZ123")
    db.add(cliente)
    db.commit()

    venta = Venta(id_cliente=cliente.id_cliente)
    db.add(venta)
    db.commit()

    resultado = db.query(Venta).filter_by(id_cliente=cliente.id_cliente).first()
    assert resultado is not None
