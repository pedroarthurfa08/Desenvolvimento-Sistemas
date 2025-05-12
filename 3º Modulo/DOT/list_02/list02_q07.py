# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um outro valor dado pertence ou não à lista.

import unittest

def verificar_valor_na_lista(lista, valor):
    return valor in lista

class TestVerificarValorNaLista(unittest.TestCase):
    def test_valor_esta_na_lista(self):
        lista = [1, 2, 3, 4, 5]
        valor = 3
        self.assertTrue(verificar_valor_na_lista(lista, valor))

    def test_valor_nao_esta_na_lista(self):
        lista = [1, 2, 3, 4, 5]
        valor = 6
        self.assertFalse(verificar_valor_na_lista(lista, valor))

if __name__ == "__main__":
    unittest.main()

'''import unittest

def verificar_valor_na_lista(lista, valor):
    return valor in lista

def main():
    lista = [10, 25, 30, 45, 50, 60, 70, 85, 90, 100]
    valor = float(input("Digite um valor para verificar se ele pertence à lista: "))
    if verificar_valor_na_lista(lista, valor):
        print(f"O valor {valor} está na lista.")
    else:
        print(f"O valor {valor} não está na lista.")

class TestVerificarValorNaLista(unittest.TestCase):
    def test_valor_esta_na_lista(self):
        lista = [1, 2, 3, 4, 5]
        valor = 3
        self.assertTrue(verificar_valor_na_lista(lista, valor))

    def test_valor_nao_esta_na_lista(self):
        lista = [1, 2, 3, 4, 5]
        valor = 6
        self.assertFalse(verificar_valor_na_lista(lista, valor))

unittest.main(exit=False)
main()'''