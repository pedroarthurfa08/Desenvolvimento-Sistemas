# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V aparece. Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.

import unittest

def contar_ocorrencias(lista, valor):
    return [i for i, x in enumerate(lista) if x == valor]

class TestContarOcorrencias(unittest.TestCase):
    def test_contar_ocorrencias(self):
        lista = [1, 2, 3, 2, 4, 2]
        valor = 2
        indices = contar_ocorrencias(lista, valor)
        self.assertEqual(indices, [1, 3, 5])

    def test_contar_ocorrencias_sem_ocorrencias(self):
        lista = [1, 2, 3, 4, 5]
        valor = 6
        indices = contar_ocorrencias(lista, valor)
        self.assertEqual(indices, [])

if __name__ == "__main__":
    unittest.main()
    
'''import unittest

def ler_lista(tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros: ")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"Elemento {i+1}: "))
                lista.append(num)
                break
            except ValueError:
                print("Resposta inválida, digite um número inteiro.")
    return lista

def contar_ocorrencias(lista, valor):
    return [i for i, x in enumerate(lista) if x == valor]

def exibir_resultado(indices, valor):
    if indices:
        print(f"\nO valor {valor} ocorre {len(indices)} vezes na lista.")
        print("Ele aparece nas posições:", indices)
    else:
        print(f"\nO valor {valor} **não aparece** na lista.")

def main():
    tamanho = 10
    W = ler_lista(tamanho)
    while True:
        try:
            V = int(input("\nDigite o valor a ser buscado na lista: "))
            break
        except ValueError:
            print("Digite um número inteiro.")
    ocorrencias = contar_ocorrencias(W, V)
    exibir_resultado(ocorrencias, V)

class TestContarOcorrencias(unittest.TestCase):
    def test_contar_ocorrencias(self):
        lista = [1, 2, 3, 2, 4, 2]
        valor = 2
        indices = contar_ocorrencias(lista, valor)
        self.assertEqual(indices, [1, 3, 5])

    def test_contar_ocorrencias_sem_ocorrencias(self):
        lista = [1, 2, 3, 4, 5]
        valor = 6
        indices = contar_ocorrencias(lista, valor)
        self.assertEqual(indices, [])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''