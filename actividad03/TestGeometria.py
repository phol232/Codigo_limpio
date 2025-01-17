import unittest

from Geometria_mejorado import GeometriaSimp

class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geometria = GeometriaSimp()

    def test_area_cuadrado(self):
        self.assertEqual(self.geometria.area(4), 16)
        self.assertEqual(self.geometria.area(0), 0)

    def test_area_rectangulo(self):
        self.assertEqual(self.geometria.area(4, 5), 20)
        self.assertEqual(self.geometria.area(3, 7), 21)

    def test_perimetro_cuadrado(self):
        self.assertEqual(self.geometria.perimetro(4), 16)
        self.assertEqual(self.geometria.perimetro(0), 0)

    def test_perimetro_rectangulo(self):
        self.assertEqual(self.geometria.perimetro(4, 5), 18)
        self.assertEqual(self.geometria.perimetro(3, 7), 20)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.geometria.area()
        with self.assertRaises(ValueError):
            self.geometria.perimetro()
        with self.assertRaises(ValueError):
            self.geometria.area(1, 2, 3)
        with self.assertRaises(ValueError):
            self.geometria.perimetro(1, 2, 3)

if __name__ == '__main__':
    unittest.main()