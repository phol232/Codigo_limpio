import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            self.productos[producto.nombre].cantidad += producto.cantidad
            logger.info(f"Se actualizó la cantidad de '{producto.nombre}' a {self.productos[producto.nombre].cantidad}.")
        else:
            self.productos[producto.nombre] = producto
            logger.info(f"Producto '{producto.nombre}' agregado al inventario.")

    def eliminar_producto(self, producto_nombre):
        if producto_nombre in self.productos:
            del self.productos[producto_nombre]
            logger.info(f"Producto '{producto_nombre}' eliminado del inventario.")
        else:
            logger.info(f"Producto '{producto_nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            logger.info("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                logger.info(str(producto))
