# 1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

import unittest

def eh_par(n):
    return n % 2 == 0

class TestParidade(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(2))
        self.assertTrue(eh_par(0))
        self.assertTrue(eh_par(100))

    def test_impar(self):
        self.assertFalse(eh_par(1))
        self.assertFalse(eh_par(3))
        self.assertFalse(eh_par(-7))

    def test_par_negativo(self):
        self.assertTrue(eh_par(-2))
        self.assertTrue(eh_par(-4))
        self.assertTrue(eh_par(-100))

if __name__ == '__main__':
    unittest.main(exit=False)

"""import unittest

def eh_par(n):
    return n % 2 == 0

class TestParidade(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(2))
        self.assertTrue(eh_par(0))
        self.assertTrue(eh_par(100))

    def test_impar(self):
        self.assertFalse(eh_par(1))
        self.assertFalse(eh_par(3))
        self.assertFalse(eh_par(-7))

    def test_par_negativo(self):
        self.assertTrue(eh_par(-2))
        self.assertTrue(eh_par(-4))
        self.assertTrue(eh_par(-100))

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            if eh_par(numero):
                print(f"{numero} é par.")
            else:
                print(f"{numero} é ímpar.")
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")"""