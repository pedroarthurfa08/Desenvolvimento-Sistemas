# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.

import unittest
import random

def gerar_numeros(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]

def separar_pares_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

class TestSepararParesImpares(unittest.TestCase):
    def test_separar_pares_impares(self):
        numeros = [1, 2, 3, 4, 5]
        pares, impares = separar_pares_impares(numeros)
        self.assertEqual(pares, [2, 4])
        self.assertEqual(impares, [1, 3, 5])

    def test_separar_pares_impares_somente_pares(self):
        numeros = [2, 4, 6, 8, 10]
        pares, impares = separar_pares_impares(numeros)
        self.assertEqual(pares, [2, 4, 6, 8, 10])
        self.assertEqual(impares, [])

    def test_separar_pares_impares_somente_impares(self):
        numeros = [1, 3, 5, 7, 9]
        pares, impares = separar_pares_impares(numeros)
        self.assertEqual(pares, [])
        self.assertEqual(impares, [1, 3, 5, 7, 9])

if __name__ == "__main__":
    unittest.main(exit=False)

    numeros = gerar_numeros(100)
    pares, impares = separar_pares_impares(numeros)

    print(f"Quantidade de números pares: {len(pares)}")
    print(f"Os números pares são: {pares}")
    print("--------------------------------------------------")
    print(f"Quantidade de números ímpares: {len(impares)}")
    print(f"Os números ímpares são: {impares}")