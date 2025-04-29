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

def exibir_menu():
    print("===== MENU ========")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")
    print("-----------------------")

def cadastra_nome(lista):
    nome = input("Digite um nome para cadastrar: ").strip()
    lista.append(nome)
    print(f"O nome '{nome}' foi cadastrado com sucesso!")

def pesquisar_nome(lista):
    nome = input("Digite o nome para pesquisar: ").strip()
    if nome in lista:
        print(f"O nome '{nome}' foi encontrado na lista.")
    else:
        print(f"O nome '{nome}' não foi encontrado na lista.")

def listar_nomes(lista):
    if lista:
        print("Lista dos nomes cadastrados:")
        for nome in lista:
            print(nome)
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

if __name__ == "__main__":
    main()