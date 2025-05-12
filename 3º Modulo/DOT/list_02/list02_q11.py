# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# =====MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0)Sair do programa
# ——————–
# Digite sua escolha:_
# 12) Deseja-se publicar

import unittest
import io
import sys

def exibir_menu():
    print("===== MENU ========")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")
    print("-----------------------")

def cadastra_nome(lista, nome):
    lista.append(nome)
    print(f"O nome '{nome}' foi cadastrado com sucesso!")

def pesquisar_nome(lista, nome):
    if nome in lista:
        print(f"O nome '{nome}' foi encontrado na lista.")
        return True
    else:
        print(f"O nome '{nome}' não foi encontrado na lista.")
        return False

def listar_nomes(lista):
    if lista:
        print("Lista dos nomes cadastrados:")
        for i, nome in enumerate(lista, start=1):
            print(f"{i}. {nome}")
        return True
    else:
        print("Não há nomes cadastrados na lista.")
        return False

def main():
    lista_nomes = []
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha: ").strip()
        if escolha == '1':
            nome = input("Digite um nome para cadastrar: ").strip().title()
            cadastra_nome(lista_nomes, nome)
        elif escolha == '2':
            nome = input("Digite o nome para pesquisar: ").strip().title()
            pesquisar_nome(lista_nomes, nome)
        elif escolha == '3':
            listar_nomes(lista_nomes)
        elif escolha == '0':
            print("Saindo do programa!")
            break
        else:
            print("Opção inválida! Tente novamente.")

class TestListaNomes(unittest.TestCase):
    def test_cadastra_nome(self):
        lista = []
        cadastra_nome(lista, "João")
        self.assertIn("João", lista)

    def test_pesquisar_nome_encontrado(self):
        lista = ["João", "Maria"]
        self.assertTrue(pesquisar_nome(lista, "João"))

    def test_pesquisar_nome_nao_encontrado(self):
        lista = ["João", "Maria"]
        self.assertFalse(pesquisar_nome(lista, "Carlos"))

    def test_listar_nomes_com_nomes(self):
        lista = ["João", "Maria"]
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertTrue(listar_nomes(lista))
        sys.stdout = sys.__stdout__
        self.assertIn("João", capturedOutput.getvalue())
        self.assertIn("Maria", capturedOutput.getvalue())

    def test_listar_nomes_vazia(self):
        lista = []
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertFalse(listar_nomes(lista))
        sys.stdout = sys.__stdout__
        self.assertIn("Não há nomes cadastrados na lista.", capturedOutput.getvalue())

if __name__ == "__main__":
    unittest.main(exit=False)
    main()
    
'''import unittest

def exibir_menu():
    print("===== MENU ========")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")
    print("-----------------------")

def cadastra_nome(lista):
    nome = input("Digite um nome para cadastrar: ").strip().title()
    lista.append(nome)
    print(f"O nome '{nome}' foi cadastrado com sucesso!")

def pesquisar_nome(lista):
    nome = input("Digite o nome para pesquisar: ").strip().title()
    if nome in lista:
        print(f"O nome '{nome}' foi encontrado na lista.")
    else:
        print(f"O nome '{nome}' não foi encontrado na lista.")

def listar_nomes(lista):
    if lista:
        print("Lista dos nomes cadastrados:")
        for i, nome in enumerate(lista, start=1):
            print(f"{i}. {nome}")
    else:
        print("Não há nomes cadastrados na lista.")

def main():
    lista_nomes = []
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha: ").strip()
        if escolha == '1':
            cadastra_nome(lista_nomes)
        elif escolha == '2':
            pesquisar_nome(lista_nomes)
        elif escolha == '3':
            listar_nomes(lista_nomes)
        elif escolha == '0':
            print("Saindo do programa!")
            break
        else:
            print("Opção inválida! Tente novamente.")

class TestListaNomes(unittest.TestCase):
    def test_cadastra_nome(self):
        lista = []
        lista.append("João")
        self.assertIn("João", lista)

    def test_pesquisar_nome(self):
        lista = ["João", "Maria"]
        self.assertIn("João", lista)

    def test_listar_nomes(self):
        lista = ["João", "Maria"]
        self.assertEqual(len(lista), 2)

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''