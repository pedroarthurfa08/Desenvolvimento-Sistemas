# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.

import unittest

def ler_lista(nome, tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros para a lista {nome}:")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"{nome}[{i+1}]: "))
                lista.append(num)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")
    return lista

def juntar_listas(lista_1, lista_2):
    return lista_1 + lista_2

def exibir_lista(nome, lista):
    print(f"Lista {nome}: {lista}")

def main():
    R = ler_lista("R", 5)
    S = ler_lista("S", 10)
    X = juntar_listas(R, S)
    exibir_lista("R", R)
    exibir_lista("S", S)
    exibir_lista("X", X)

class TestJuntarListas(unittest.TestCase):
    def test_juntar_listas(self):
        lista_1 = [1, 2, 3]
        lista_2 = [4, 5, 6]
        lista_juntada = juntar_listas(lista_1, lista_2)
        self.assertEqual(lista_juntada, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()