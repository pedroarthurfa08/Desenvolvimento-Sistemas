import unittest
from circulo import area, perimetro

class TestCirculo(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.14)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), 12.56)

    def test_perimetro(self):
        self.assertAlmostEqual(perimetro(1), 6.28)
        self.assertAlmostEqual(perimetro(0), 0)
        self.assertAlmostEqual(perimetro(2), 12.56)

if __name__ == '__main__':
    unittest.main()