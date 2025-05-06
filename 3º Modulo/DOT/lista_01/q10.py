# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
#a) A função Max recebe como parâmetros de entrada 4  números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
#b) O programa principal lê 4 séries de 4 números a, b, c, d Para cada série lida imprime o maior dos quatro números usando a função Max.

import unittest

def maximo(a, b, c, d):
    return max(a, b, c, d)

class TestMaximo(unittest.TestCase):
    def test_numeros_positivos(self):
        self.assertEqual(maximo(1, 2, 3, 4), 4)

    def test_numeros_negativos(self):
        self.assertEqual(maximo(-1, -2, -3, -4), -1)

    def test_numeros_iguais(self):
        self.assertEqual(maximo(5, 5, 5, 5), 5)

if __name__ == '__main__':
    unittest.main(exit=False)

    for i in range(1, 5):
        while True:
            try:
                print(f"\n**** Série de 4 números (Conjunto {i}) ****")
                num1 = int(input("\nDigite o primeiro número: "))
                num2 = int(input("\nDigite o segundo número: "))
                num3 = int(input("\nDigite o terceiro número: "))
                num4 = int(input("\nDigite o quarto número: "))
                print(f"\n----> O maior número é: {maximo(num1, num2, num3, num4)}")
                break
            except ValueError:
                print("\nErro! Por favor, digite um número inteiro válido.")