# 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)

import unittest

def calculo_S(N):
    if N <= 0:
        raise ValueError("N deve ser um valor inteiro positivo.")
    return sum((t ** 2 + 1) / (t + 3) for t in range(1, N + 1))

class TestCalculoS(unittest.TestCase):
    def test_calculo_S_positivo(self):
        self.assertAlmostEqual(calculo_S(4), 4.380952380952381)

    def test_calculo_S_um(self):
        self.assertAlmostEqual(calculo_S(1), 0.5)

    def test_calculo_S_invalido(self):
        with self.assertRaises(ValueError):
            calculo_S(-1)

if __name__ == '__main__':
    unittest.main(exit=False)
    
'''import unittest

def calculo_S(N):
    if N <= 0:
        raise ValueError("N deve ser um valor inteiro positivo.")
    return sum((t ** 2 + 1) / (t + 3) for t in range(1, N + 1))

class TestCalculoS(unittest.TestCase):
    def test_calculo_S_positivo(self):
        self.assertAlmostEqual(calculo_S(4), 4.380952380952381)

    def test_calculo_S_um(self):
        self.assertAlmostEqual(calculo_S(1), 0.5)

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