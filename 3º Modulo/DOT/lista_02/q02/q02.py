# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.

def analisa_numeros(numeros):
    qnt_negativos = 0
    soma_positivos = 0

    for numero in numeros:
        if numero < 0:
            qnt_negativos += 1 
        elif numero > 0:
            soma_positivos += 1

    print("A quantidade de números negativos é", qnt_negativos)
    print("A soma dos números positivos é", soma_positivos)