'''Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.'''
lista1 = []
lista2 = []
for i in range(10):
    elemento = int(input())
    lista1.append(elemento)
for i in range(10):
    elemento = int(input())
    lista2.append(elemento)
uniao = []
for elemento in lista1:
    if elemento not in uniao:
        uniao.append(elemento)
for elemento in lista2:
    if elemento not in uniao:
        uniao.append(elemento)
print(uniao)