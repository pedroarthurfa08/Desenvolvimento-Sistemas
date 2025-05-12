# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assimpor diante. Escrever todo a lista D e todo a lista E.

import unittest

def inverter_lista(lista):
    return lista[::-1]

def ler_lista(tamanho):
    # Esta função contém input(), que você pediu para remover.
    # Para os testes, não precisamos dela.
    return [0] * tamanho  # Retorna uma lista preenchida com zeros para evitar erros nos testes

class TestInverterLista(unittest.TestCase):
    def test_inverter_lista(self):
        lista = [1, 2, 3, 4, 5]
        lista_invertida = inverter_lista(lista)
        self.assertEqual(lista_invertida, [5, 4, 3, 2, 1])

    def test_inverter_lista_vazia(self):
        lista = []
        lista_invertida = inverter_lista(lista)
        self.assertEqual(lista_invertida, [])

if __name__ == "__main__":
    unittest.main()
    
'''import unittest

def inverter_lista(lista):
    return lista[::-1]

def ler_lista(tamanho):
    return [int(input(f'Elemento {i + 1}: ')) for i in range(tamanho)]

def main():
    tamanho = 10
    D = ler_lista(tamanho)
    E = inverter_lista(D)
    print('Lista D:', D)
    print('Lista E (inversa):', E)

class TestInverterLista(unittest.TestCase):
    def test_inverter_lista(self):
        lista = [1, 2, 3, 4, 5]
        lista_invertida = inverter_lista(lista)
        self.assertEqual(lista_invertida, [5, 4, 3, 2, 1])

    def test_inverter_lista_vazia(self):
        lista = []
        lista_invertida = inverter_lista(lista)
        self.assertEqual(lista_invertida, [])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''