# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes ocorreu a letra ‘A’.
#OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

import unittest

def validar_entrada(entrada):
    return entrada.isalpha()

def contar_letras_a(lista_letras):
    return lista_letras.count('A')

class TestContarLetrasA(unittest.TestCase):
    def test_contar_letras_a(self):
        lista_letras = list("ABACA")
        self.assertEqual(contar_letras_a(lista_letras), 3)

    def test_contar_letras_a_sem_a(self):
        lista_letras = list("BCDE")
        self.assertEqual(contar_letras_a(lista_letras), 0)

if __name__ == "__main__":
    unittest.main()

'''import unittest

def validar_entrada(entrada):
    return entrada.isalpha()

def contar_letras_a(lista_letras):
    return lista_letras.count('A')

def main():
    while True:
        entrada_usuario = input("Digite uma lista de letras (sem espaços ou números): ").strip().upper()
        if validar_entrada(entrada_usuario):
            break
        print("Entrada inválida. A lista deve conter apenas letras.")
    
    lista_letras = list(entrada_usuario)
    contagem_a = contar_letras_a(lista_letras)
    print(f"A letra 'A' aparece {contagem_a} vezes na lista.")

class TestContarLetrasA(unittest.TestCase):
    def test_contar_letras_a(self):
        lista_letras = list("ABACA")
        self.assertEqual(contar_letras_a(lista_letras), 3)

    def test_contar_letras_a_sem_a(self):
        lista_letras = list("BCDE")
        self.assertEqual(contar_letras_a(lista_letras), 0)

unittest.main(exit=False)
main()'''