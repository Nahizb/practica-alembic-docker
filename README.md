# Práctica: Migraciones con Python + Alembic + Docker + PostgreSQL

Entorno listo para practicar el ciclo completo de migraciones como en un proyecto profesional.

## Estructura del proyecto

```
practica_alembic_docker/
├── app/
│   ├── __init__.py
│   └── models/
│       ├── __init__.py      # Base declarativa + import de todos los modelos
│       ├── autor.py
│       └── libro.py
├── alembic/
│   ├── env.py                # configuración de conexión y metadata
│   ├── script.py.mako        # plantilla de cada migración nueva
│   └── versions/             # aquí se van generando las migraciones
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── seed_data.sql
└── README.md
```

---

## Paso 0: Preparar el entorno

```bash
cp .env.example .env
```

No necesitas tocar nada más del `.env` para empezar; ya apunta al servicio `db` de docker-compose.

## Paso 1: Levantar los contenedores

```bash
docker-compose up -d --build
```

Esto levanta:
- **db**: PostgreSQL 16, expuesto en `localhost:5433` (usuario `postgres`, password `5432`, db `postgres`)
  > Se usa el puerto **5433** en tu máquina (host) para no chocar con el Postgres local que ya tienes corriendo en 5432. Dentro de la red de Docker, el contenedor `app` sigue hablando con `db:5432` sin problema — esto solo afecta si te conectas desde fuera de Docker (por ejemplo con pgAdmin o DBeaver en tu máquina).
- **app**: contenedor Python con Alembic y SQLAlchemy instalados, con tu código montado como volumen

Verifica que ambos estén corriendo:

```bash
docker-compose ps
```

## Paso 2: Entrar al contenedor de la app

Todos los comandos de Alembic los vas a correr **dentro** del contenedor `app`, no en tu máquina local:

```bash
docker-compose exec app bash
```

A partir de aquí, ya estás dentro del contenedor (verás el prompt cambiar).

## Paso 3: Generar tu primera migración (autogenerada)

Dentro del contenedor:

```bash
alembic revision --autogenerate -m "crear tablas autores y libros"
```

Esto compara tus modelos (`app/models/`) contra la base de datos vacía y genera un archivo en `alembic/versions/`.

**Abre ese archivo generado y revísalo antes de aplicarlo** — este es el hábito profesional más importante. Confirma que:
- Los nombres de tabla y columnas son correctos
- Los tipos de datos tienen sentido
- El `downgrade()` realmente revierte lo que hace el `upgrade()`

## Paso 4: Aplicar la migración

```bash
alembic upgrade head
```

Verifica desde tu máquina (fuera del contenedor) que las tablas se crearon:

```bash
docker-compose exec db psql -U postgres -d postgres -c "\dt"
```

## Paso 5: Cargar datos de prueba

Simula que ya tienes datos "reales" en producción:

```bash
docker-compose exec -T db psql -U postgres -d postgres < seed_data.sql
```

Verifica:

```bash
docker-compose exec db psql -U postgres -d postgres -c "SELECT * FROM autores;"
```

## Paso 6: Practicar una migración incremental (lo más importante)

Con datos ya cargados, ahora modifica el modelo. Por ejemplo, agrega un campo `email` a `Autor` en `app/models/autor.py`:

```python
email = Column(String(120))
```

Genera la migración (dentro del contenedor):

```bash
alembic revision --autogenerate -m "agregar email a autores"
```

Revisa el archivo generado y aplícalo:

```bash
alembic upgrade head
```

Confirma que los datos siguen intactos y la columna nueva apareció:

```bash
docker-compose exec db psql -U postgres -d postgres -c "SELECT * FROM autores;"
```

## Paso 7: Practicar el rollback

```bash
alembic downgrade -1
```

Verifica que la columna `email` desapareció pero los datos de las filas siguen ahí. Luego vuelve a subir:

```bash
alembic upgrade head
```

## Paso 8: Practicar una migración manual (sin autogenerate)

Este es el ejercicio más realista. Crea una migración vacía:

```bash
alembic revision -m "migrar nacionalidad a tabla paises"
```

Alembic te da un archivo con `upgrade()` y `downgrade()` vacíos. Aquí es donde tú escribes la lógica a mano: crear la tabla `paises`, poblarla a partir de los valores distintos que ya existen en `autores.nacionalidad`, agregar la FK, y finalmente eliminar la columna vieja. Este tipo de migración con transformación de datos (no solo de esquema) es el que más se parece a los retos reales de un equipo.

Si quieres, en el siguiente mensaje te ayudo a escribir esa migración paso a paso.

## Comandos de referencia

```bash
alembic current              # versión actual del esquema
alembic history --verbose    # historial completo de migraciones
alembic downgrade base       # revertir todo hasta el inicio
alembic upgrade +1           # subir solo una versión
```

## Apagar todo

```bash
docker-compose down          # detiene los contenedores, conserva los datos
docker-compose down -v       # detiene y BORRA también el volumen de datos (reinicio total)
```
