# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.

def ler_lista(nome, tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros para a lista {nome}:")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"{nome}[{i}]: "))
                lista.append(num)
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")
    return lista

def juntar_listas (lista_1, lista_2):
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
main()