from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .clientes import Cliente              # noqa: E402,F401
from .puestos import Puesto                # noqa: E402,F401
from .trabajadores import Trabajador       # noqa: E402,F401
from .ventas import Venta                  # noqa: E402,F401
from .productos import Producto            # noqa: E402,F401
from .detalle_ventas import DetalleVenta   # noqa: E402,F401
from .departamentos import Departamento
from .proveedores import Proveedor          # noqa: E402,F401