BEGIN;

-- Running upgrade 7b704a24b23a -> 5d8adb70ef6a

CREATE INDEX ix_productos_categoria ON productos (categoria);

UPDATE alembic_version SET version_num='5d8adb70ef6a' WHERE alembic_version.version_num = '7b704a24b23a';

COMMIT;

