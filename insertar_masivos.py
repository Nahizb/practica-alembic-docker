import random
from sqlalchemy import create_engine, text
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

DATABASE_URL = "postgresql://postgres:5432@localhost:5433/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

random.seed(42)  # reproducible: mismos datos "aleatorios" cada vez que lo corras

# ============================
# LIMPIAR TODO ANTES DE SEMBRAR (equivalente al TRUNCATE que veniamos haciendo)
# ============================
session.execute(text("""
    TRUNCATE detalle_ventas, ventas, trabajadores, clientes,
             puestos, departamentos, proveedores, productos
    RESTART IDENTITY CASCADE
"""))
session.commit()
print("Tablas limpiadas.")

# ============================
# PROVEEDORES (10)
# ============================
nombres_empresa = [
    "TechSupply", "Distribuidora Norte", "Global Electronics", "MegaStock",
    "ImportPro", "Andina Comercial", "SurTech", "Nexo Digital",
    "Punto Mayorista", "Cadena Iberica",
]
proveedores_creados = []
for i, nombre in enumerate(nombres_empresa, start=1):
    p = Proveedor(
        nombre_proveedor=f"{nombre} S.A.",
        contacto_email=f"contacto{i}@{nombre.lower().replace(' ', '')}.com",
        telefono=f"555-{1000+i}",
    )
    session.add(p)
    proveedores_creados.append(p)
session.commit()
print(f"Proveedores insertados: {len(proveedores_creados)}")

# ============================
# DEPARTAMENTOS (8)
# ============================
departamentos_data = [
    ("Finanzas", "Control de gastos y presupuestos"),
    ("Recursos Humanos", "Gestion de personal y contrataciones"),
    ("Logistica", "Coordinacion de envios y almacenamiento"),
    ("Marketing", "Promocion y estrategias de mercado"),
    ("IT", "Infraestructura tecnologica y soporte"),
    ("Ventas", "Gestion comercial y atencion al cliente"),
    ("Legal", "Asuntos juridicos y cumplimiento normativo"),
    ("Compras", "Adquisicion de insumos y negociacion con proveedores"),
]
for nombre, descripcion in departamentos_data:
    session.add(Departamento(nombre_departamento=nombre, descripcion=descripcion))
session.commit()
print(f"Departamentos insertados: {len(departamentos_data)}")

# ============================
# PUESTOS (6)
# ============================
nombres_puestos = ["Cajero", "Supervisora", "Vendedor", "Gerente", "Almacenista", "Analista"]
puestos_creados = {}
for nombre_puesto in nombres_puestos:
    puesto = Puesto(nombre_puesto=nombre_puesto)
    session.add(puesto)
    session.flush()
    puestos_creados[nombre_puesto] = puesto
session.commit()
print(f"Puestos insertados: {len(puestos_creados)}")

# ============================
# CLIENTES (50)
# ============================
nombres_pila = [
    "Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Laura",
    "Diego", "Elena", "Miguel", "Patricia", "Javier", "Carmen", "Andres",
    "Isabel", "Ricardo", "Lucia", "Fernando", "Paula",
]
apellidos = [
    "Perez", "Lopez", "Sanchez", "Torres", "Ramirez", "Gomez", "Castillo",
    "Fernandez", "Diaz", "Martinez", "Herrera", "Rivas", "Ortiz", "Morales",
    "Vega", "Castro", "Rojas", "Silva", "Nunez", "Guerrero",
]
clientes_creados = {}
for i in range(1, 51):
    nombre_completo = f"{random.choice(nombres_pila)} {random.choice(apellidos)}"
    dni = f"{10000000 + i}{random.choice('ABCDEFGHIJKLM')}"  # garantiza unicidad via el contador i
    telefono = f"6{random.randint(10000000, 99999999)}"
    cliente = Cliente(nombre_cliente=nombre_completo, dni_cliente=dni, telefono=telefono)
    session.add(cliente)
    session.flush()
    clientes_creados[cliente.id_cliente] = cliente
session.commit()
print(f"Clientes insertados: {len(clientes_creados)}")

# ============================
# TRABAJADORES (30)
# ============================
trabajadores_creados = []
for i in range(1, 31):
    nombre_completo = f"{random.choice(nombres_pila)} {random.choice(apellidos)}"
    puesto = random.choice(list(puestos_creados.values()))
    email = f"{nombre_completo.lower().replace(' ', '.')}{i}@empresa.com"
    trabajador = Trabajador(nombre=nombre_completo, puesto=puesto, email=email)
    session.add(trabajador)
    trabajadores_creados.append(trabajador)
session.commit()
print(f"Trabajadores insertados: {len(trabajadores_creados)}")

# ============================
# PRODUCTOS (40)
# ============================
tipos_producto = [
    "Laptop", "Mouse", "Teclado", "Monitor", "Impresora", "Router",
    "Disco SSD", "Memoria RAM", "Tablet", "Auriculares", "Webcam",
    "Altavoz", "Cargador", "Cable HDMI", "Silla ergonomica",
]
categorias = ["Electronica", "Oficina", "Accesorios", "Redes", "Almacenamiento"]
productos_creados = {}
for i in range(1, 41):
    nombre_producto = f"{random.choice(tipos_producto)} Modelo {i}"
    precio = round(random.uniform(10, 1200), 2)
    categoria = random.choice(categorias)
    stock = random.randint(0, 150)
    producto = Producto(
        nombre_producto=nombre_producto, precio_unitario=precio,
        categoria=categoria, stock=stock,
    )
    session.add(producto)
    session.flush()
    productos_creados[producto.id_producto] = producto
session.commit()
print(f"Productos insertados: {len(productos_creados)}")

# ============================
# VENTAS (100)
# ============================
ventas_creadas = []
ids_clientes = list(clientes_creados.keys())
for _ in range(100):
    id_cliente = random.choice(ids_clientes)
    venta = Venta(id_cliente=id_cliente)
    session.add(venta)
    ventas_creadas.append(venta)
session.commit()
print(f"Ventas insertadas: {len(ventas_creadas)}")

# ============================
# DETALLE_VENTAS (250)
# ============================
ids_productos = list(productos_creados.keys())
detalles_creados = 0
for venta in ventas_creadas:
    # cada venta tiene entre 1 y 4 lineas de producto
    for _ in range(random.randint(1, 4)):
        id_producto = random.choice(ids_productos)
        producto = productos_creados[id_producto]
        cantidad = random.randint(1, 5)
        detalle = DetalleVenta(
            id_venta=venta.id_venta,
            id_producto=id_producto,
            cantidad=cantidad,
            precio_unitario=producto.precio_unitario,
        )
        session.add(detalle)
        detalles_creados += 1
session.commit()
print(f"Detalles de venta insertados: {detalles_creados}")

print("\n=== SIEMBRA MASIVA COMPLETADA ===")