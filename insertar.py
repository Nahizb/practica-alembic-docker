from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.clientes import Cliente
from app.models.trabajadores import Trabajador
from app.models.puestos import Puesto
from app.models.ventas import Venta
from app.models.departamentos import Departamento
from app.models.productos import Producto
from app.models.proveedores import Proveedor
from app.models.detalle_ventas import DetalleVenta
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
    ("Juan Pérez", "12345678A", "612345789"),
    ("María López", "87654321B", "634892117"),
    ("Carlos Sánchez", "11223344C", "698441203"),
    ("Ana Torres", "55667788D", "622908554"),
    ("Luis Ramírez", "99887766E", "645771902"),
    ("Sofía Gómez", "44556677F", "677540129"),
    ("Pedro Castillo", "22334455G", "693218447"),
    ("Laura Fernández", "66778899H", "656709331"),
]


clientes_creados = {}

for nombre, dni, telefono in clientes:
    cliente = Cliente(nombre_cliente=nombre, dni_cliente=dni,  telefono=telefono)
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
# INSERTAR PRODUCTOS
# ============================

productos = [
    ("Laptop", 899.99, "Electronica", 15),
    ("Mouse", 15.50, "Electronica", 120),
    ("Teclado", 45.00, "Electronica", 80),
    ("Monitor", 210.00, "Electronica", 30),
]
productos_creados = {}
for nombre, precio, categoria, stock in productos:
    producto = Producto(nombre_producto=nombre, precio_unitario=precio, categoria=categoria, stock=stock)
    session.add(producto)
    session.flush()
    productos_creados[nombre] = producto
session.commit()
print("Productos insertados correctamente.")


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

# ============================
# INSERTAR DETALLE_VENTAS
# ============================

detalles = [
    ("Juan Pérez", "Laptop", 1),
    ("Juan Pérez", "Mouse", 2),
    ("María López", "Monitor", 1),
    ("Carlos Sánchez", "Teclado", 1),
    ("Ana Torres", "Mouse", 1),
]

for nombre_cliente, nombre_producto, cantidad in detalles:
    venta = next(v for v in ventas_creadas if v.id_cliente == clientes_creados[nombre_cliente].id_cliente)
    producto = productos_creados[nombre_producto]

    detalle = DetalleVenta(
        id_venta=venta.id_venta,
        id_producto=producto.id_producto,
        cantidad=cantidad,
        precio_unitario=producto.precio_unitario
    )

    session.add(detalle)

session.commit()
print("Detalles de ventas insertados correctamente.")
