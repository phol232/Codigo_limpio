import unittest
from InventarioMejorado import Producto, Inventario


class TestInventario(unittest.TestCase):

    def setUp(self):
        self.producto1 = Producto("Manzanas", 1.5, 10)
        self.producto2 = Producto("Naranjas", 2.0, 5)
        self.producto3 = Producto("Manzanas", 1.5, 15)
        self.inventario = Inventario()

    def test_agregar_producto_nuevo(self):
        self.inventario.agregar_producto(self.producto1)
        self.assertIn("Manzanas", self.inventario.productos)
        self.assertEqual(self.inventario.productos["Manzanas"].cantidad, 10)

    def test_agregar_producto_existente(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto3)
        self.assertEqual(self.inventario.productos["Manzanas"].cantidad, 25)

    def test_eliminar_producto_existente(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.eliminar_producto("Manzanas")
        self.assertNotIn("Manzanas", self.inventario.productos)

    def test_eliminar_producto_inexistente(self):
        self.inventario.agregar_producto(self.producto2)
        self.inventario.eliminar_producto("Manzanas")
        self.assertIn("Naranjas", self.inventario.productos)
        self.assertEqual(len(self.inventario.productos), 1)

    def test_mostrar_inventario_vacio(self):
        with self.assertLogs(level='INFO') as log:
            self.inventario.mostrar_inventario()
        self.assertIn("El inventario está vacío.", log.output[0])

    def test_mostrar_inventario_con_productos(self):
        self.inventario.agregar_producto(self.producto1)
        with self.assertLogs(level='INFO') as log:
            self.inventario.mostrar_inventario()
        self.assertIn("Producto: Manzanas, Precio: 1.5, Cantidad: 10", log.output[0])


if __name__ == "__main__":
    unittest.main()
