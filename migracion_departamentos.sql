BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e0b801f668bf

CREATE TABLE autores (
    id SERIAL NOT NULL, 
    nombre VARCHAR(100) NOT NULL, 
    nacionalidad VARCHAR(50), 
    PRIMARY KEY (id)
);

CREATE TABLE libros (
    id SERIAL NOT NULL, 
    titulo VARCHAR(200) NOT NULL, 
    anio_publicacion INTEGER, 
    autor_id INTEGER, 
    creado_en TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(autor_id) REFERENCES autores (id)
);

INSERT INTO alembic_version (version_num) VALUES ('e0b801f668bf') RETURNING alembic_version.version_num;

-- Running upgrade e0b801f668bf -> 48f3f16ec316

CREATE TABLE clientes (
    id_cliente SERIAL NOT NULL, 
    nombre_cliente VARCHAR(45) NOT NULL, 
    PRIMARY KEY (id_cliente)
);

CREATE TABLE trabajadores (
    id_trabajador SERIAL NOT NULL, 
    nombre VARCHAR(45) NOT NULL, 
    puesto VARCHAR(45) NOT NULL, 
    PRIMARY KEY (id_trabajador)
);

CREATE TABLE ventas (
    id_venta SERIAL NOT NULL, 
    id_cliente INTEGER NOT NULL, 
    PRIMARY KEY (id_venta), 
    FOREIGN KEY(id_cliente) REFERENCES clientes (id_cliente)
);

UPDATE alembic_version SET version_num='48f3f16ec316' WHERE alembic_version.version_num = 'e0b801f668bf';

-- Running upgrade 48f3f16ec316 -> 8097bfe59908

ALTER TABLE trabajadores ADD COLUMN email VARCHAR(45);

UPDATE trabajadores SET email = 'robert10@gmail.com' WHERE nombre = 'Roberto Díaz';

UPDATE trabajadores SET email = 'elena10@gmail.com' WHERE nombre = 'Elena Martínez';

UPDATE trabajadores SET email = 'miguel@gmail.com' WHERE nombre = 'Miguel Herrera';

UPDATE trabajadores SET email = 'patricia@gmail.com' WHERE nombre = 'Patricia Rivas';

ALTER TABLE trabajadores ALTER COLUMN email SET NOT NULL;

UPDATE alembic_version SET version_num='8097bfe59908' WHERE alembic_version.version_num = '48f3f16ec316';

-- Running upgrade 8097bfe59908 -> 77accdf32ec1

ALTER TABLE clientes ADD COLUMN dni_cliente VARCHAR(12);

UPDATE clientes SET dni_cliente = '12345678A' WHERE nombre_cliente = 'Juan Pérez';

UPDATE clientes SET dni_cliente = '87654321B' WHERE nombre_cliente = 'María López';

UPDATE clientes SET dni_cliente = '11223344C' WHERE nombre_cliente = 'Carlos Sánchez';

UPDATE clientes SET dni_cliente = '55667788D' WHERE nombre_cliente = 'Ana Torres';

UPDATE clientes SET dni_cliente = '99887766E' WHERE nombre_cliente = 'Luis Ramírez';

UPDATE clientes SET dni_cliente = '44556677F' WHERE nombre_cliente = 'Sofía Gómez';

UPDATE clientes SET dni_cliente = '22334455G' WHERE nombre_cliente = 'Pedro Castillo';

UPDATE clientes SET dni_cliente = '66778899H' WHERE nombre_cliente = 'Laura Fernández';

ALTER TABLE clientes ALTER COLUMN dni_cliente SET NOT NULL;

UPDATE alembic_version SET version_num='77accdf32ec1' WHERE alembic_version.version_num = '8097bfe59908';

-- Running upgrade 77accdf32ec1 -> f75b74569381

ALTER TABLE clientes ADD CONSTRAINT clientes_dni_cliente_key UNIQUE (dni_cliente);

UPDATE alembic_version SET version_num='f75b74569381' WHERE alembic_version.version_num = '77accdf32ec1';

-- Running upgrade f75b74569381 -> c77a574e633f

CREATE TABLE puestos (
    id_puesto SERIAL NOT NULL, 
    nombre_puesto VARCHAR(45) NOT NULL, 
    PRIMARY KEY (id_puesto), 
    UNIQUE (nombre_puesto)
);

INSERT INTO puestos (nombre_puesto) VALUES ('Cajero');

INSERT INTO puestos (nombre_puesto) VALUES ('Supervisora');

INSERT INTO puestos (nombre_puesto) VALUES ('Vendedor');

INSERT INTO puestos (nombre_puesto) VALUES ('Gerente');

ALTER TABLE trabajadores ADD COLUMN id_puesto INTEGER;

UPDATE trabajadores
        SET id_puesto = puestos.id_puesto
        FROM puestos
        WHERE trabajadores.puesto = puestos.nombre_puesto;

ALTER TABLE trabajadores ALTER COLUMN id_puesto SET NOT NULL;

ALTER TABLE trabajadores ADD CONSTRAINT fk_trabajadores_puesto FOREIGN KEY(id_puesto) REFERENCES puestos (id_puesto);

ALTER TABLE trabajadores DROP COLUMN puesto;

UPDATE alembic_version SET version_num='c77a574e633f' WHERE alembic_version.version_num = 'f75b74569381';

-- Running upgrade c77a574e633f -> 64bd56eb4166

CREATE TABLE productos (
    id_producto SERIAL NOT NULL, 
    nombre_producto VARCHAR(100) NOT NULL, 
    precio_unitario NUMERIC(10, 2) NOT NULL, 
    PRIMARY KEY (id_producto)
);

CREATE TABLE detalle_ventas (
    id_detalle SERIAL NOT NULL, 
    id_venta INTEGER NOT NULL, 
    id_producto INTEGER NOT NULL, 
    cantidad INTEGER NOT NULL, 
    precio_unitario NUMERIC(10, 2) NOT NULL, 
    PRIMARY KEY (id_detalle), 
    FOREIGN KEY(id_producto) REFERENCES productos (id_producto), 
    FOREIGN KEY(id_venta) REFERENCES ventas (id_venta)
);

UPDATE alembic_version SET version_num='64bd56eb4166' WHERE alembic_version.version_num = 'c77a574e633f';

-- Running upgrade 64bd56eb4166 -> 9bb05211070e

ALTER TABLE productos ADD COLUMN categoria VARCHAR(50);

UPDATE alembic_version SET version_num='9bb05211070e' WHERE alembic_version.version_num = '64bd56eb4166';

-- Running upgrade 64bd56eb4166 -> 2c229a6f1c99

ALTER TABLE productos ADD COLUMN stock INTEGER DEFAULT '0' NOT NULL;

INSERT INTO alembic_version (version_num) VALUES ('2c229a6f1c99') RETURNING alembic_version.version_num;

-- Running upgrade 2c229a6f1c99, 9bb05211070e -> 7b704a24b23a

DELETE FROM alembic_version WHERE alembic_version.version_num = '2c229a6f1c99';

UPDATE alembic_version SET version_num='7b704a24b23a' WHERE alembic_version.version_num = '9bb05211070e';

-- Running upgrade 7b704a24b23a -> 5d8adb70ef6a

CREATE INDEX ix_productos_categoria ON productos (categoria);

UPDATE alembic_version SET version_num='5d8adb70ef6a' WHERE alembic_version.version_num = '7b704a24b23a';

-- Running upgrade 5d8adb70ef6a -> eee2a84596d3

DROP INDEX ix_productos_nombre;

CREATE INDEX ix_productos_nombre_producto ON productos (nombre_producto);

UPDATE alembic_version SET version_num='eee2a84596d3' WHERE alembic_version.version_num = '5d8adb70ef6a';

-- Running upgrade eee2a84596d3 -> 7edc9946ec1d

CREATE TABLE departamentos (
    id_departamento SERIAL NOT NULL, 
    nombre_departamento VARCHAR(50) NOT NULL, 
    descripcion VARCHAR(200), 
    PRIMARY KEY (id_departamento)
);

UPDATE alembic_version SET version_num='7edc9946ec1d' WHERE alembic_version.version_num = 'eee2a84596d3';

COMMIT;

