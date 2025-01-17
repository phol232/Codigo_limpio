import unittest
from X_mejorado import X_mej

class Test_X(unittest.TestCase):
    def setUp(self):
        self.x = X_mej()

    def test_X_numerosDiferentesCero(self):
        self.assertEqual(12, self.x.z(3, 4))

    def test_X_segun_parametroCero(self):
        self.assertEqual("Error: División por cero no permitida", self.x.z(3, 0))

if __name__ == '__main__':
    unittest.main()