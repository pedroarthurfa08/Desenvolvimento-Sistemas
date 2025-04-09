# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os elementos deste em uma outra lista de 20 elementos.

lista1 = []
lista2 = []

for i in range(10):
    valor = int(input(f"Lista 01 - Valor {i + 1}: "))
    lista1.append(valor)

for i in range(10):
    valor = int(input(f"Lista 02 - Valor {i + 1}: "))
    lista2.append(valor)

lista_intercalada = []

for i in range(10):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i]) 

print("Lista intercalada:")
print(lista_intercalada)