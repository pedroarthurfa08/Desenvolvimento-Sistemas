# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro.

import unittest

def fatorial(f):
    if f < 0:
        raise ValueError("Não existe fatorial de número negativo.")
    fat = 1
    for i in range(1, f + 1):
        fat *= i
    return fat

class TestFatorial(unittest.TestCase):
    def test_fatorial_0(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_1(self):
        self.assertEqual(fatorial(1), 1)

    def test_fatorial_5(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_7(self):
        self.assertEqual(fatorial(7), 5040)

    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-1)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            num = int(input("\nDigite um número: "))
            print(f"\nO fatorial de {num} é: {fatorial(num)}")
            break
        except ValueError as e:
            print(f"\n{e}")
