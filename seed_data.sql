-- Ejecuta esto DESPUÉS de correr "alembic upgrade head" la primera vez
-- Simula datos ya existentes en "producción" para practicar migraciones sobre datos reales

INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez', 'Colombiana'),
('Isabel Allende', 'Chilena'),
('Jorge Luis Borges', 'Argentina'),
('Julio Cortázar', 'Argentina');

INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES
('Cien años de soledad', 1967, 1),
('El amor en los tiempos del cólera', 1985, 1),
('La casa de los espíritus', 1982, 2),
('Ficciones', 1944, 3),
('Rayuela', 1963, 4),
('El aleph', 1949, 3);
