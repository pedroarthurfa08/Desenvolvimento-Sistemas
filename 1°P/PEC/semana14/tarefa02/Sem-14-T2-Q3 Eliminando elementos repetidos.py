'''Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando elementos repetidos'''
def remove_repetidos(lista):
    lista_unica = []
    for numero in lista:
        if numero not in lista_unica:
            lista_unica.append(numero)
    return lista_unica
def ler_lista():
    lista = []
    for i in range(20):
        numero = int(input())
        lista.append(numero)
    return lista
lista_numeros = ler_lista()
lista_sem_repetidos = remove_repetidos(lista_numeros)
print(lista_sem_repetidos)