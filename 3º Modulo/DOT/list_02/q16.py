# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.

import unittest

def transformar_lista(lista_x):
    return [x / 2 if i % 2 == 0 else x * 3 for i, x in enumerate(lista_x)]

class TestTransformarLista(unittest.TestCase):
    def test_transformar_lista(self):
        lista_x = [2, 3, 4, 5]
        lista_y = transformar_lista(lista_x)
        self.assertEqual(lista_y, [1, 9, 2, 15])

if __name__ == "__main__":
    unittest.main()
    
'''import unittest

def ler_lista(tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros e positivos: ")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"Elemento {i+1}: "))
                if num > 0:
                    lista.append(num)
                    break
                else:
                    print("O número deve ser positivo.")
            except ValueError:
                print("Resposta inválida, digite um número inteiro.")
    return lista

def transformar_lista(lista_x):
    return [x / 2 if i % 2 == 0 else x * 3 for i, x in enumerate(lista_x)]

def exibir_listas(lista_x, lista_y):
    print("\nLista X:", lista_x)
    print("Lista Y:", lista_y)

def main():
    tamanho = 10
    X = ler_lista(tamanho)
    Y = transformar_lista(X)
    exibir_listas(X, Y)

class TestTransformarLista(unittest.TestCase):
    def test_transformar_lista(self):
        lista_x = [2, 3, 4, 5]
        lista_y = transformar_lista(lista_x)
        self.assertEqual(lista_y, [1, 9, 2, 15])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''