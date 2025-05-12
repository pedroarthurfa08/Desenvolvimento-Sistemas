# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
#a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
#b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.

import unittest

def Max(num1, num2):
    """
    Recebe dois números inteiros e retorna o maior.
    Se forem iguais, retorna qualquer um deles.
    """
    if num1 > num2:
        return num1
    else:
        return num2

class TestMax(unittest.TestCase):
    def test_maior_primeiro(self):
        self.assertEqual(Max(5, 2), 5)

    def test_maior_segundo(self):
        self.assertEqual(Max(3, 7), 7)

    def test_iguais_positivo(self):
        self.assertEqual(Max(4, 4), 4)

    def test_iguais_negativo(self):
        self.assertEqual(Max(-2, -2), -2)

    def test_negativo_maior(self):
        self.assertEqual(Max(-1, -5), -1)

    def test_negativo_menor(self):
        self.assertEqual(Max(-10, -3), -3)

    def test_positivo_negativo(self):
        self.assertEqual(Max(10, -5), 10)

    def test_negativo_positivo(self):
        self.assertEqual(Max(-8, 2), 2)

if __name__ == '__main__':
    unittest.main(exit=False)