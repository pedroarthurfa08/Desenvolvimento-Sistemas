# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face. 

import unittest
import random

def contar_ocorrencias(resultados):
    contagem_lados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for resultado in resultados:
        if 1 <= resultado <= 6:
            contagem_lados[resultado] += 1
    return contagem_lados

def lancar_dado(n):
    return [random.randint(1, 6) for _ in range(n)]

class TestContarOcorrencias(unittest.TestCase):
    def test_contar_ocorrencias(self):
        resultados = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
        contagem_lados = contar_ocorrencias(resultados)
        self.assertEqual(contagem_lados[1], 2)
        self.assertEqual(contagem_lados[2], 2)
        self.assertEqual(contagem_lados[3], 2)
        self.assertEqual(contagem_lados[4], 2)
        self.assertEqual(contagem_lados[5], 2)
        self.assertEqual(contagem_lados[6], 2)

if __name__ == "__main__":
    unittest.main()

'''import unittest
import random

def contar_ocorrencias(resultados):
    contagem_lados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for resultado in resultados:
        if 1 <= resultado <= 6:
            contagem_lados[resultado] += 1
    return contagem_lados

def lancar_dado(n):
    return [random.randint(1, 6) for _ in range(n)]

def main():
    n = int(input("Digite o número de lançamentos do dado: "))
    resultados = lancar_dado(n)
    contagem_lados = contar_ocorrencias(resultados)
    for face, contagem in contagem_lados.items():
        print(f'Face {face}: {contagem} ocorrência(s)')

class TestContarOcorrencias(unittest.TestCase):
    def test_contar_ocorrencias(self):
        resultados = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
        contagem_lados = contar_ocorrencias(resultados)
        self.assertEqual(contagem_lados[1], 2)
        self.assertEqual(contagem_lados[2], 2)
        self.assertEqual(contagem_lados[3], 2)
        self.assertEqual(contagem_lados[4], 2)
        self.assertEqual(contagem_lados[5], 2)
        self.assertEqual(contagem_lados[6], 2)

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''