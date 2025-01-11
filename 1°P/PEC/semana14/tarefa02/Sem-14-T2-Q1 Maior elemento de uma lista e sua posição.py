'''Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior elemento e a posição que ele se encontra.'''
numeros = []
for i in range(10):
    num = int(input())
    numeros.append(num)
maior_numero = numeros[0]
posicao_maior = 0
for i in range(1, len(numeros)):
    if numeros[i] > maior_numero:
        maior_numero = numeros[i]
        posicao_maior = i
print(numeros)
print(maior_numero) 
print(posicao_maior)
