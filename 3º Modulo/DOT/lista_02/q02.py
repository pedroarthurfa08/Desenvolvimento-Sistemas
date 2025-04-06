# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.

n = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1.5, -2.3, 4.0, -1.1, 3.3, 0.0, -4.5, 2.2, -3.3, 5.5]

qnt_negativos = 0
soma_positivos = 0

for numero in n:
    if numero < 0:
        qnt_negativos += 1 
    elif numero > 0:
        soma_positivos += 1

print("A quantidade de números negativos é", qnt_negativos)
print("A noma dos números positivo é", soma_positivos)