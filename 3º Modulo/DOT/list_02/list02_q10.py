# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

import unittest
import random

def gerar_lista(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

def mostrar_maior_menor(lista):
    maior_elemento = max(lista)
    posicao_maior = lista.index(maior_elemento)
    menor_elemento = min(lista)
    posicao_menor = lista.index(menor_elemento)
    return maior_elemento, posicao_maior, menor_elemento, posicao_menor

class TestMostrarMaiorMenor(unittest.TestCase):
    def test_mostrar_maior_menor(self):
        lista = [1, 2, 3, 4, 5]
        maior_elemento, posicao_maior, menor_elemento, posicao_menor = mostrar_maior_menor(lista)
        self.assertEqual(maior_elemento, 5)
        self.assertEqual(posicao_maior, 4)
        self.assertEqual(menor_elemento, 1)
        self.assertEqual(posicao_menor, 0)

if __name__ == "__main__":
    unittest.main()
    
'''import unittest
import random

def gerar_lista(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

def mostrar_maior_menor(lista):
    maior_elemento = max(lista)
    posicao_maior = lista.index(maior_elemento)
    menor_elemento = min(lista)
    posicao_menor = lista.index(menor_elemento)
    return maior_elemento, posicao_maior, menor_elemento, posicao_menor

def main():
    lista = gerar_lista(15)
    print("Lista:", lista)
    maior_elemento, posicao_maior, menor_elemento, posicao_menor = mostrar_maior_menor(lista)
    print(f"O maior elemento é {maior_elemento} e está na posição {posicao_maior}.")
    print(f"O menor elemento é {menor_elemento} e está na posição {posicao_menor}.")

class TestMostrarMaiorMenor(unittest.TestCase):
    def test_mostrar_maior_menor(self):
        lista = [1, 2, 3, 4, 5]
        maior_elemento, posicao_maior, menor_elemento, posicao_menor = mostrar_maior_menor(lista)
        self.assertEqual(maior_elemento, 5)
        self.assertEqual(posicao_maior, 4)
        self.assertEqual(menor_elemento, 1)
        self.assertEqual(posicao_menor, 0)

unittest.main(exit=False)
main()'''