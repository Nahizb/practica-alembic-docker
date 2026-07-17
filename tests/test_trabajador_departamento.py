def test_trabajador_departamento_nm(db):
    from app.models.trabajadores import Trabajador
    from app.models.departamentos import Departamento
    from app.models.puestos import Puesto
    from app.models.trabajador_departamento import TrabajadorDepartamento

    puesto = Puesto(nombre_puesto="Analista")
    db.add(puesto)
    db.flush()

    trabajador = Trabajador(nombre="Test Trabajador", puesto=puesto, email="test@empresa.com")
    depto1 = Departamento(nombre_departamento="IT", descripcion="Infraestructura")
    depto2 = Departamento(nombre_departamento="Ventas", descripcion="Comercial")
    db.add_all([trabajador, depto1, depto2])
    db.flush()

    asignacion1 = TrabajadorDepartamento(trabajador=trabajador, departamento=depto1, rol="Miembro")
    asignacion2 = TrabajadorDepartamento(trabajador=trabajador, departamento=depto2, rol="Colaborador")
    db.add_all([asignacion1, asignacion2])
    db.commit()

    assert len(trabajador.departamentos) == 2
    assert len(depto1.trabajadores) == 1
    assert asignacion1.rol == "Miembro"