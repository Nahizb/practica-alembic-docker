from sqlalchemy import text

def test_indice_departamentos(db):
    resultado = db.execute(text("""
        SELECT indexname
        FROM pg_indexes
        WHERE tablename='departamentos'
        AND indexname='idx_departamento_nombre';
    """)).fetchone()

    assert resultado is not None
