import unittest
import q01

class TestParImpar(unittest.TestCase):

    def test_par(self):
        self.assertTrue(q01.par_impar(2))
        self.assertTrue(q01.par_impar(0))
        self.assertTrue(q01.par_impar(-4))

    def test_impar(self):
        self.assertFalse(q01.par_impar(1))
        self.assertFalse(q01.par_impar(-3))
        self.assertFalse(q01.par_impar(7))

if __name__ == '__main__':
    unittest.main()