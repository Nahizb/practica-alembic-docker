from app.models.trabajadores import Trabajador
from app.models.puestos import Puesto

def test_insertar_trabajador(db):
    puesto_obj = Puesto(nombre_puesto="Cajero Test")
    db.add(puesto_obj)
    db.commit()

    trabajador = Trabajador(
        nombre="Roberto Díaz",
        puesto=puesto_obj,
        email="robert10@gmail.com"
    )
    db.add(trabajador)
    db.commit()

    resultado = db.query(Trabajador).filter_by(email="robert10@gmail.com").first()
    assert resultado.puesto.nombre_puesto == "Cajero Test"
