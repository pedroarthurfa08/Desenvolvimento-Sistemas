# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

'''import unittest

def contar_divisores(n):
    if n <= 0:
        raise ValueError("O número deve ser inteiro e positivo.")
    divisores = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                divisores += 1
            else:
                divisores += 2
    return divisores

class TestContarDivisores(unittest.TestCase):
    def test_numero_primo(self):
        self.assertEqual(contar_divisores(7), 2)

    def test_numero_composto(self):
        self.assertEqual(contar_divisores(12), 6)

    def test_numero_quadrado_perfeito(self):
        self.assertEqual(contar_divisores(16), 5)

    def test_numero_invalido(self):
        with self.assertRaises(ValueError):
            contar_divisores(-1)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            num = int(input("\nDigite um número inteiro e positivo: "))
            print(f"\nO número digitado tem {contar_divisores(num)} divisores.")
            break
        except ValueError as e:
            print(f"\n{e}")'''