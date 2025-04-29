import unittest
from q04 import avaliacao

class TestAvaliador(unittest.TestCase):
    def test_aprovado(self):
        aprovado, media = avaliacao(7, 8)
        self.assertTrue(aprovado)
        self.assertEqual(media, 7.5)

    def test_reprovado(self):
        aprovado, media = avaliacao(5, 5)
        self.assertFalse(aprovado)
        self.assertEqual(media, 5.0)

    def test_limiar(self):
        aprovado, media = avaliacao(6, 6)
        self.assertTrue(aprovado)
        self.assertEqual(media, 6.0)

if __name__ == '__main__':
    unittest.main()