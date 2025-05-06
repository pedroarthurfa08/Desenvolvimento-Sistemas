# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

import unittest

def somatorio(n):
    if n <= 0:
        raise ValueError("O número deve ser inteiro e positivo")
    return n * (n + 1) // 2

class TestSomatorio(unittest.TestCase):
    def test_somatorio_positivo(self):
        self.assertEqual(somatorio(5), 15)

    def test_somatorio_um(self):
        self.assertEqual(somatorio(1), 1)

    def test_somatorio_invalido(self):
        with self.assertRaises(ValueError):
            somatorio(-1)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            num = int(input('\nDigite um número inteiro e positivo: '))
            print(f"\nO número digitado tem um somatório igual a {somatorio(num)}")
            break
        except ValueError as e:
            print(f"\n{e}")