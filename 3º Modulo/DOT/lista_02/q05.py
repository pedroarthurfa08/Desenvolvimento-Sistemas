# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os elementos deste em uma outra lista de 20 elementos.

def encontrar_maior_menor(lista):
    if not lista:
        print("A lista está vazia.")
        return

    maior = max(lista)
    menor = min(lista)

    posicao_maior = lista.index(maior)
    posicao_menor = lista.index(menor)

    print(f"\nO maior elemento é {maior} e está na posição {posicao_maior}.")
    print(f"O menor elemento é {menor} e está na posição {posicao_menor}.")

def coletar_numeros(qnt=15):
    numeros = []
    for i in range(qnt):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        numeros.append(valor)
    return numeros

lista = coletar_numeros()
encontrar_maior_menor(lista)