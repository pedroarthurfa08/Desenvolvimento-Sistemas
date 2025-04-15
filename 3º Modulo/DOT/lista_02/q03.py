# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à daleitura.

def ler_e_imprimir_invertido():
    import random  

    n = int(input("\nQual a quantidade de números? "))
    numeros = []

    for _ in range(n):
        num = float(input("Digite um número: "))
        numeros.append(num)

    print("\nNúmeros em ordem inversa:")
    for num in reversed(numeros):
        print(num)

ler_e_imprimir_invertido()