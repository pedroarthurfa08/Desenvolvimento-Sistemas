# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à daleitura.

import random

n = int(input("\nQual a quantidade de números?"))

numeros = []

for _ in range(n):
    num = float(input("Digite um número: "))
    numeros.append(num)

#print(numeros[::-1])

    #or

for num in reversed(numeros):
    print(num)