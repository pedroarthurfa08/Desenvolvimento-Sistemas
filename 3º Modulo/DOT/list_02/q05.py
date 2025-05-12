# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os elementos deste em uma outra lista de 20 elementos.

import unittest

def coletar_numeros(qnt):
    numeros = []
    for i in range(qnt):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        numeros.append(valor)
    return numeros

def intercalar_listas(lista1, lista2):
    return [valor for par in zip(lista1, lista2) for valor in par]

def main():
    print("Digite os valores da primeira lista:")
    lista1 = coletar_numeros(10)
    print("\nDigite os valores da segunda lista:")
    lista2 = coletar_numeros(10)

    lista_intercalada = intercalar_listas(lista1, lista2)

    print("\nLista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista Intercalada:", lista_intercalada)

class TestIntercalarListas(unittest.TestCase):
    def test_intercalar_listas(self):
        lista1 = [1, 3, 5]
        lista2 = [2, 4, 6]
        lista_intercalada = intercalar_listas(lista1, lista2)
        self.assertEqual(lista_intercalada, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main(exit=False)

'''import unittest

def coletar_numeros(qnt):
    numeros = []
    for i in range(qnt):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        numeros.append(valor)
    return numeros

def intercalar_listas(lista1, lista2):
    return [valor for par in zip(lista1, lista2) for valor in par]

def main():
    print("Digite os valores da primeira lista:")
    lista1 = coletar_numeros(10)
    print("\nDigite os valores da segunda lista:")
    lista2 = coletar_numeros(10)

    lista_intercalada = intercalar_listas(lista1, lista2)

    print("\nLista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista Intercalada:", lista_intercalada)

class TestIntercalarListas(unittest.TestCase):
    def test_intercalar_listas(self):
        lista1 = [1, 3, 5]
        lista2 = [2, 4, 6]
        lista_intercalada = intercalar_listas(lista1, lista2)
        self.assertEqual(lista_intercalada, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''