import unittest
from Procesador_Mejorado import ProcesadorMej

class TestProcesadorMej(unittest.TestCase):
    def setUp(self):
        self.procesador = ProcesadorMej()

    def test_productoSuma(self):
        self.assertEqual(self.procesador.productoSuma(2, 3, 4), 10)
        self.assertEqual(self.procesador.productoSuma(1, 0, 5), 5)
        self.assertEqual(self.procesador.productoSuma(-1, 3, 2), -1)

    def test_cuadradodeunNumero(self):
        self.assertEqual(self.procesador.cuadradodeunNumero(3), 9)
        self.assertEqual(self.procesador.cuadradodeunNumero(0), 0)
        self.assertEqual(self.procesador.cuadradodeunNumero(-2), 4)

if __name__ == '__main__':
    unittest.main()