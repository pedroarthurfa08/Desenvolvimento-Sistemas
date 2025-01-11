def adicionar_nomes(tipo, genero, lista_nomes):
    """Função para adicionar nomes à lista com base no tipo e gênero do animal."""
    if tipo == 'cachorro':
        if genero == 'macho':
            lista_nomes.append("Rex")
        else:
            lista_nomes.append("Luna")
    elif tipo == 'gato':
        if genero == 'macho':
            lista_nomes.append("Tom")
        else:
            lista_nomes.append("Mia")
    else:
        print("Tipo de animal desconhecido.")
        
def remover_nome(nome, lista_nomes):
    """Função para remover um nome da lista."""
    if nome in lista_nomes:
        lista_nomes.remove(nome)
        print(f"Nome {nome} removido.")
    else:
        print(f"O nome {nome} não está na lista.")
        
def escolher_nomes():
    """Função principal para gerenciar o processo de escolha de nomes."""
    print("Serviço de escolha de nome para animais de estimação")
    lista_nomes = []
    
    try:
        num_animais = int(input("Quantos animais você precisa dar nome? "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    for i in range(num_animais):
        tipo = input("Qual o tipo do animal (cachorro/gato)? ").lower()
        genero = input("O animal é macho ou fêmea? ").lower()
        adicionar_nomes(tipo, genero, lista_nomes)
    
    while True:
        print("\nLista de nomes atuais:", lista_nomes)
        opcao = input("Deseja adicionar ou remover um nome? (adicionar/remover/finalizar): ").lower()
        if opcao == 'adicionar':
            tipo = input("Qual o tipo do animal (cachorro/gato)? ").lower()
            genero = input("O animal é macho ou fêmea? ").lower()
            adicionar_nomes(tipo, genero, lista_nomes)
        elif opcao == 'remover':
            nome = input("Qual nome você gostaria de remover? ")
            remover_nome(nome, lista_nomes)
        elif opcao == 'finalizar':
            break
        else:
            print("Opção inválida, tente novamente.")
    
    print("Você deve chamar seu(s) animal(is) de:", ", ".join(lista_nomes))

escolher_nomes()
