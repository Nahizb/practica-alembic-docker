from app.models.clientes import Cliente

def test_insertar_cliente(db):
    cliente = Cliente(nombre_cliente="Nahizbeth", dni_cliente="123ABC")
    db.add(cliente)
    db.commit()

    resultado = db.query(Cliente).filter_by(dni_cliente="123ABC").first()
    assert resultado is not None
    assert resultado.nombre_cliente == "Nahizbeth"
