# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

def mostrar_maior_menor(lista):
    maior_elemento = max(lista)
    posicao_maior = lista.index(maior_elemento)

    menor_elemento = min(lista)
    posicao_menor = lista.index(menor_elemento)

    print(f"O maior elemento é {maior_elemento} e está na posição {posicao_maior}.")
    print(f"O menor elemento é {menor_elemento} e está na posição {posicao_menor}.")