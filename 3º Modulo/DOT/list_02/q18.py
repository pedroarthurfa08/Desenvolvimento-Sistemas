# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

import unittest

def ler_lista(tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros (positivos ou negativos):")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"Elemento {i+1}: "))
                lista.append(num)
                break
            except ValueError:
                print("Resposta inválida, digite um número inteiro.")
    return lista

def filtrar_negativos(lista):
    return [num for num in lista if num < 0]

def exibir_lista(lista_x, lista_r):
    print("\nLista X:", lista_x)
    print("Lista R (somente negativos):", lista_r)

def main():
    tamanho = 10
    X = ler_lista(tamanho)
    R = filtrar_negativos(X)
    exibir_lista(X, R)

class TestFiltrarNegativos(unittest.TestCase):
    def test_filtrar_negativos(self):
        lista = [1, -2, 3, -4, 5]
        negativos = filtrar_negativos(lista)
        self.assertEqual(negativos, [-2, -4])

    def test_filtrar_negativos_sem_negativos(self):
        lista = [1, 2, 3, 4, 5]
        negativos = filtrar_negativos(lista)
        self.assertEqual(negativos, [])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()