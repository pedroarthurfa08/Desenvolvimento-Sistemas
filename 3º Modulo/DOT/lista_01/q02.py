# 2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo. Área = PI * r2; Perímetro = PI * 2 * r;

"""import unittest
import math

def area(r):
    return math.pi * r ** 2

def perimetro(r):
    return math.pi * 2 * r

class TestCirculo(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimetro(self):
        self.assertAlmostEqual(perimetro(1), 2 * math.pi)
        self.assertAlmostEqual(perimetro(0), 0)
        self.assertAlmostEqual(perimetro(2), 4 * math.pi)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            raio = float(input("Digite o valor do raio: "))
            if raio < 0:
                print("O raio não pode ser negativo.")
            else:
                print(f"\nA área do círculo é: {area(raio):.2f}")
                print(f"O perímetro do círculo é: {perimetro(raio):.2f}")
                break
        except ValueError:
            print("\nEntrada inválida. Digite um número válido.")"""

import unittest
import math

def area(r):
    return math.pi * r ** 2

def perimetro(r):
    return math.pi * 2 * r

class TestCirculo(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimetro(self):
        self.assertAlmostEqual(perimetro(1), 2 * math.pi)
        self.assertAlmostEqual(perimetro(0), 0)
        self.assertAlmostEqual(perimetro(2), 4 * math.pi)

if __name__ == '__main__':
    unittest.main(exit=False)