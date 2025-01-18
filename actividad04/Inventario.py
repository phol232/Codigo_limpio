class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto_nombre):
        self.productos = [p for p in self.productos if p.nombre != producto_nombre]

    def mostrar_inventario(self):
        for producto in self.productos:
            producto.mostrar_detalles()  



producto1 = Producto("Manzanas", 1.5, 10)
producto2 = Producto("Naranjas", 2.0, 5)

inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

print("Inventario actual:")
inventario.mostrar_inventario()

inventario.eliminar_producto("Manzanas")
print("\nInventario después de eliminar 'Manzanas':")
inventario.mostrar_inventario()
