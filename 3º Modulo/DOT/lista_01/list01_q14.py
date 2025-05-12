# 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + 1/1! + ½! + 1/3! + 1 /N!

import unittest
import math

def calculo_S(N):
    if N <= 0:
        raise ValueError("N deve ser um valor inteiro positivo.")
    return 1 + sum(1 / math.factorial(i) for i in range(1, N + 1))

class TestCalculoS(unittest.TestCase):
    def test_calculo_S_positivo(self):
        self.assertAlmostEqual(calculo_S(4), 2.708333333333333)

    def test_calculo_S_um(self):
        self.assertAlmostEqual(calculo_S(1), 2)

    def test_calculo_S_invalido(self):
        with self.assertRaises(ValueError):
            calculo_S(-1)

if __name__ == '__main__':
    unittest.main(exit=False)

'''import unittest
import math

def calculo_S(N):
    if N <= 0:
        raise ValueError("N deve ser um valor inteiro positivo.")
    return 1 + sum(1 / math.factorial(i) for i in range(1, N + 1))

class TestCalculoS(unittest.TestCase):
    def test_calculo_S_positivo(self):
        self.assertAlmostEqual(calculo_S(4), 2.708333333333333)

    def test_calculo_S_um(self):
        self.assertAlmostEqual(calculo_S(1), 2)

    def test_calculo_S_invalido(self):
        with self.assertRaises(ValueError):
            calculo_S(-1)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            N = int(input("\nDigite um número inteiro positivo: "))
            print(f"O valor de S é {calculo_S(N):.4f}")
            break
        except ValueError as e:
            print(f"\n{e}")'''