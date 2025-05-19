# 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime o número de vezes que cada número ocorre na sequência.

import unittest
from collections import Counter

def contar_ocorrencias(numeros):
    return Counter(numeros)

class TestContarOcorrencias(unittest.TestCase):
    def test_contar_ocorrencias(self):
        numeros = [1, 2, 2, 3, 3, 3]
        ocorrencias = contar_ocorrencias(numeros)
        self.assertEqual(ocorrencias[1], 1)
        self.assertEqual(ocorrencias[2], 2)
        self.assertEqual(ocorrencias[3], 3)

    def test_contar_ocorrencias_sem_repeticoes(self):
        numeros = [1, 2, 3, 4, 5]
        ocorrencias = contar_ocorrencias(numeros)
        self.assertEqual(len(ocorrencias), 5)

    def test_contar_ocorrencias_todos_repetidos(self):
        numeros = [1, 1, 1, 1, 1]
        ocorrencias = contar_ocorrencias(numeros)
        self.assertEqual(ocorrencias[1], 5)

    def test_contar_ocorrencias_lista_vazia(self):
        numeros = []
        ocorrencias = contar_ocorrencias(numeros)
        self.assertEqual(len(ocorrencias), 0)

if __name__ == "__main__":
    unittest.main()