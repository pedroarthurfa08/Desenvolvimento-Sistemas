# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

import unittest

def encontrar_maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    posicao_maior = lista.index(maior)
    posicao_menor = lista.index(menor)
    return maior, posicao_maior, menor, posicao_menor

def main():
    lista = []
    for i in range(15):
        while True:
            try:
                valor = int(input(f"Digite o {i + 1}º valor: "))
                lista.append(valor)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro.")

    maior, posicao_maior, menor, posicao_menor = encontrar_maior_menor(lista)

    print(f"\nO maior elemento é {maior} e está na posição {posicao_maior}.")
    print(f"O menor elemento é {menor} e está na posição {posicao_menor}.")

class TestEncontrarMaiorMenor(unittest.TestCase):
    def test_encontrar_maior_menor(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        maior, posicao_maior, menor, posicao_menor = encontrar_maior_menor(lista)
        self.assertEqual(maior, 15)
        self.assertEqual(posicao_maior, 14)
        self.assertEqual(menor, 1)
        self.assertEqual(posicao_menor, 0)

if __name__ == "__main__":
    unittest.main(exit=False)
    
'''import unittest

def encontrar_maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    posicao_maior = lista.index(maior)
    posicao_menor = lista.index(menor)
    return maior, posicao_maior, menor, posicao_menor

def main():
    lista = []
    for i in range(15):
        while True:
            try:
                valor = int(input(f"Digite o {i + 1}º valor: "))
                lista.append(valor)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro.")

    maior, posicao_maior, menor, posicao_menor = encontrar_maior_menor(lista)

    print(f"\nO maior elemento é {maior} e está na posição {posicao_maior}.")
    print(f"O menor elemento é {menor} e está na posição {posicao_menor}.")

class TestEncontrarMaiorMenor(unittest.TestCase):
    def test_encontrar_maior_menor(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        maior, posicao_maior, menor, posicao_menor = encontrar_maior_menor(lista)
        self.assertEqual(maior, 15)
        self.assertEqual(posicao_maior, 14)
        self.assertEqual(menor, 1)
        self.assertEqual(posicao_menor, 0)

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''