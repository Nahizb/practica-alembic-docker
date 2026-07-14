-- Running upgrade 473ff287d787 -> b2a6059b3066

CREATE TABLE proveedores (
    id_proveedor SERIAL NOT NULL, 
    nombre_proveedor VARCHAR(150) NOT NULL, 
    contacto_email VARCHAR(150), 
    telefono VARCHAR(20), 
    PRIMARY KEY (id_proveedor)
);

CREATE UNIQUE INDEX ix_proveedores_nombre_proveedor ON proveedores (nombre_proveedor);

DROP INDEX idx_departamento_nombre;

UPDATE alembic_version SET version_num='b2a6059b3066' WHERE alembic_version.version_num = '473ff287d787';

