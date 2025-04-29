# 2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo. Área = PI * r2; Perímetro = PI * 2 * r;

import unittest

def area(r):
    return 3.14 * r ** 2

def perimetro(r):
    return 3.14 * 2 * r

if __name__ == '__main__':
    try:
        raio = float(input("Digite o valor do raio: "))
        print(f"\nA área do círculo é: {area(raio):.2f}")
        print(f"O perímetro do círculo é: {perimetro(raio):.2f}")
    except ValueError:
        print("\nEntrada inválida. Digite um número válido.")

class TestCirculo(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.14)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), 12.56)

    def test_perimetro(self):
        self.assertAlmostEqual(perimetro(1), 6.28)
        self.assertAlmostEqual(perimetro(0), 0)
        self.assertAlmostEqual(perimetro(2), 12.56)