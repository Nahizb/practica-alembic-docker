from sqlalchemy import text


def test_indice_departamentos(db):
    resultado = db.execute(text("""
        SELECT indexname
        FROM pg_indexes
        WHERE tablename = 'departamentos'
        AND indexname = 'ix_departamentos_nombre_departamento';
    """)).fetchone()
    assert resultado is not None