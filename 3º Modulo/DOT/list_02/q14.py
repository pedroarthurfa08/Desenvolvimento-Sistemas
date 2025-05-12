# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.

import unittest

def modificar_lista(lista):
    return [x if x >= 0 else 0 for x in lista]

def ler_lista(tamanho):
    return [int(input(f'Elemento {i + 1}: ')) for i in range(tamanho)]

def main():
    tamanho = 10
    C = ler_lista(tamanho)
    C_modificada = modificar_lista(C)
    print("Lista C modificada:", C_modificada)

class TestModificarLista(unittest.TestCase):
    def test_modificar_lista(self):
        lista = [-1, 2, -3, 4, -5]
        lista_modificada = modificar_lista(lista)
        self.assertEqual(lista_modificada, [0, 2, 0, 4, 0])

    def test_modificar_lista_sem_negativos(self):
        lista = [1, 2, 3, 4, 5]
        lista_modificada = modificar_lista(lista)
        self.assertEqual(lista_modificada, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()