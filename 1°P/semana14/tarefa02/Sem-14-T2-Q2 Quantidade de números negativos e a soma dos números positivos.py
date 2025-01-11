'''Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de números negativos e a soma dos números positivos dessa lista.'''
numeros = []
for i in range(10):
    num = int(input())
    numeros.append(num)
negativos = 0
soma_positivos = 0
for num in numeros:
    if num < 0:
        negativos += 1
    elif num > 0:
        soma_positivos += num
print(numeros)
print(f"{negativos}")
print(f"{soma_positivos}")
