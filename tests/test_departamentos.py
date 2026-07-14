from app.models.departamentos import Departamento

def test_insertar_departamento(db):
    dep = Departamento(
        nombre_departamento="Recursos Humanos",
        descripcion="Departamento encargado de la gestión del personal"
    )
    db.add(dep)
    db.commit()

    resultado = db.query(Departamento).filter_by(nombre_departamento="Recursos Humanos").first()
    assert resultado is not None
    assert resultado.descripcion.startswith("Departamento")
