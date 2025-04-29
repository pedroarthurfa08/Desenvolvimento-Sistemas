import unittest
from q03 import celsius

class TestConversor(unittest.TestCase):
    def test_celsius(self):
        self.assertAlmostEqual(celsius(32), 0)
        self.assertAlmostEqual(celsius(212), 100)
        self.assertAlmostEqual(celsius(98.6), 37, places=1)

if __name__ == '__main__':
    unittest.main()