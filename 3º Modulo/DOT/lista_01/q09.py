# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

import unittest

def soma_intervalo(a, b):
    soma = 0
    for i in range(a, b + 1):
        soma += i
    return soma

class TestSomaIntervalo(unittest.TestCase):
    def test_soma_intervalo_positivos(self):
        self.assertEqual(soma_intervalo(1, 5), 15)

    def test_soma_intervalo_negativos(self):
        self.assertEqual(soma_intervalo(-5, -1), -15)

    def test_soma_intervalo_misto(self):
        self.assertEqual(soma_intervalo(-2, 2), 0)

    def test_soma_intervalo_igual(self):
        self.assertEqual(soma_intervalo(5, 5), 5)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            n1 = int(input('\nDigite o primeiro número: '))
            n2 = int(input('\nDigite o segundo número: '))
            if n1 <= n2:
                print(f'\nA soma do intervalo [{n1}, {n2}] é {soma_intervalo(n1, n2)}')
                break
            else:
                print('\nn2 deve ser maior ou igual a n1. Digite novamente!')
        except ValueError:
            print('\nAlgo de errado não está certo, tente novamente.')