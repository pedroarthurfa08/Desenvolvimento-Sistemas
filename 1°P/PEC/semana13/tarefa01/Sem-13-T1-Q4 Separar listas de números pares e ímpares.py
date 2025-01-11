'''Leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas'''
numeros = []
pares = []
impares = []
for i in range(20):
    numero = int(input())
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(numeros)
print(pares)
print(impares)