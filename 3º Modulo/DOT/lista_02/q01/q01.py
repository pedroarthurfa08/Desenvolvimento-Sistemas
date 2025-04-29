# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.

numeros = list(range(100))

pares = []
impares= []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Quantidade de número pares", len(pares))
print("Os números pares são", pares)

print("--------------------------------------------------")

print("Quantidade de número impares", len(impares))
print("Os números impares são", impares)