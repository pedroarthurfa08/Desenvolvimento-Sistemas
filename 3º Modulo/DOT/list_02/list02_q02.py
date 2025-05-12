# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.

import unittest
import random

def gerar_numeros(tamanho):
    return [random.uniform(-100, 100) for _ in range(tamanho)]

def analisa_numeros(numeros):
    qnt_negativos = sum(1 for numero in numeros if numero < 0)
    soma_positivos = sum(numero for numero in numeros if numero > 0)
    return qnt_negativos, soma_positivos

class TestAnalisaNumeros(unittest.TestCase):
    def test_analisa_numeros(self):
        numeros = [-1, 2, -3, 4, -5]
        qnt_negativos, soma_positivos = analisa_numeros(numeros)
        self.assertEqual(qnt_negativos, 3)
        self.assertEqual(soma_positivos, 6)

    def test_analisa_numeros_somente_negativos(self):
        numeros = [-1, -2, -3, -4, -5]
        qnt_negativos, soma_positivos = analisa_numeros(numeros)
        self.assertEqual(qnt_negativos, 5)
        self.assertEqual(soma_positivos, 0)

    def test_analisa_numeros_somente_positivos(self):
        numeros = [1, 2, 3, 4, 5]
        qnt_negativos, soma_positivos = analisa_numeros(numeros)
        self.assertEqual(qnt_negativos, 0)
        self.assertEqual(soma_positivos, 15)

if __name__ == "__main__":
    unittest.main(exit=False)

'''import unittest
import random

def gerar_numeros(tamanho):
    return [random.uniform(-100, 100) for _ in range(tamanho)]

def analisa_numeros(numeros):
    qnt_negativos = sum(1 for numero in numeros if numero < 0)
    soma_positivos = sum(numero for numero in numeros if numero > 0)
    return qnt_negativos, soma_positivos

class TestAnalisaNumeros(unittest.TestCase):
    def test_analisa_numeros(self):
        numeros = [-1, 2, -3, 4, -5]
        qnt_negativos, soma_positivos = analisa_numeros(numeros)
        self.assertEqual(qnt_negativos, 3)
        self.assertEqual(soma_positivos, 6)

    def test_analisa_numeros_somente_negativos(self):
        numeros = [-1, -2, -3, -4, -5]
        qnt_negativos, soma_positivos = analisa_numeros(numeros)
        self.assertEqual(qnt_negativos, 5)
        self.assertEqual(soma_positivos, 0)

    def test_analisa_numeros_somente_positivos(self):
        numeros = [1, 2, 3, 4, 5]
        qnt_negativos, soma_positivos = analisa_numeros(numeros)
        self.assertEqual(qnt_negativos, 0)
        self.assertEqual(soma_positivos, 15)

if __name__ == "__main__":
    unittest.main(exit=False)

    numeros = gerar_numeros(10)
    qnt_negativos, soma_positivos = analisa_numeros(numeros)

    print(f"Quantidade de números negativos: {qnt_negativos}")
    print(f"Soma dos números positivos: {soma_positivos:.2f}")
    print(f"Números: {numeros}")'''