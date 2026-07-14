from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.clientes import Cliente
from app.models.trabajadores import Trabajador
from app.models.puestos import Puesto
from app.models.ventas import Venta
from app.models.departamentos import Departamento
from app.models.proveedores import Proveedor
from app.models import Base

# Conexión al PostgreSQL del contenedor Docker
DATABASE_URL = "postgresql://postgres:5432@localhost:5433/postgres"
engine = create_engine("postgresql://postgres:5432@localhost:5433/postgres")

Session = sessionmaker(bind=engine)
session = Session()


#============================
#INSERTAR PROVEEDORES
#==========================


proveedores = [
    ("TechSupply S.A.", "ventas@techsupply.com", "555-0101"),
    ("Distribuidora Norte", "contacto@distnorte.com", "555-0102"),
    ("Global Electronics", "info@globalelec.com", "555-0103"),
]

for nombre, email, telefono in proveedores:
    p = Proveedor(nombre_proveedor=nombre, contacto_email=email, telefono=telefono)
    session.add(p)

session.commit()
print("Proveedores insertados correctamente.")

# ============================
# INSERTAR DEPARTAMENTOS
# ============================

nuevos_departamentos = [
    ("Finanzas", "Control de gastos y presupuestos"),
    ("Recursos Humanos", "Gestión de personal y contrataciones"),
    ("Logística", "Coordinación de envíos y almacenamiento"),
    ("Marketing", "Promoción y estrategias de mercado"),
    ("IT", "Infraestructura tecnológica y soporte"),
]

for nombre, descripcion in nuevos_departamentos:
    dep = Departamento(
        nombre_departamento=nombre,
        descripcion=descripcion
    )
    session.add(dep)

session.commit()
print("Departamentos insertados correctamente.")


# ============================
# INSERTAR CLIENTES
# ============================

clientes = [
    ("Juan Pérez", "12345678A"),
    ("María López", "87654321B"),
    ("Carlos Sánchez", "11223344C"),
    ("Ana Torres", "55667788D"),
    ("Luis Ramírez", "99887766E"),
    ("Sofía Gómez", "44556677F"),
    ("Pedro Castillo", "22334455G"),
    ("Laura Fernández", "66778899H"),
]

clientes_creados = {}

for nombre, dni in clientes:
    cliente = Cliente(nombre_cliente=nombre, dni_cliente=dni)
    session.add(cliente)
    session.flush()
    clientes_creados[nombre] = cliente

session.commit()
print("Clientes insertados correctamente.")

# ============================
# INSERTAR PUESTOS
# ============================

puestos = ["Cajero", "Supervisora", "Vendedor", "Gerente"]
puestos_creados = {}

for nombre_puesto in puestos:
    puesto = Puesto(nombre_puesto=nombre_puesto)
    session.add(puesto)
    session.flush()
    puestos_creados[nombre_puesto] = puesto

session.commit()
print("Puestos insertados correctamente.")

# ============================
# INSERTAR TRABAJADORES
# ============================

trabajadores = [
    ("Roberto Díaz", "Cajero", "robert10@gmail.com"),
    ("Elena Martínez", "Supervisora", "elena10@gmail.com"),
    ("Miguel Herrera", "Vendedor", "miguel@gmail.com"),
    ("Patricia Rivas", "Gerente", "patricia@gmail.com"),
]

trabajadores_creados = {}

for nombre, puesto_nombre, email in trabajadores:
    trabajador = Trabajador(
        nombre=nombre,
        puesto=puestos_creados[puesto_nombre],  # relación correcta
        email=email
    )
    session.add(trabajador)
    session.flush()
    trabajadores_creados[nombre] = trabajador

session.commit()
print("Trabajadores insertados correctamente.")

# ============================
# INSERTAR VENTAS
# ============================

ventas = ["Juan Pérez", "María López", "Carlos Sánchez", "Ana Torres"]

ventas_creadas = []

for nombre_cliente in ventas:
    venta = Venta(id_cliente=clientes_creados[nombre_cliente].id_cliente)
    session.add(venta)
    ventas_creadas.append(venta)

session.commit()
print("Ventas insertadas correctamente.")
