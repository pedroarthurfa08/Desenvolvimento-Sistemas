# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

import unittest

def inverter_lista(lista):
    return lista[::-1]

def main():
    lista_x = [1, 2, 3, 4, 5]
    lista_y = inverter_lista(lista_x)
    print("Lista x:", lista_x)
    print("Lista y (invertida):", lista_y)

class TestInverterLista(unittest.TestCase):
    def test_inverter_lista(self):
        lista = [1, 2, 3, 4, 5]
        lista_invertida = inverter_lista(lista)
        self.assertEqual(lista_invertida, [5, 4, 3, 2, 1])

    def test_inverter_lista_vazia(self):
        lista = []
        lista_invertida = inverter_lista(lista)
        self.assertEqual(lista_invertida, [])

unittest.main(exit=False)
main()