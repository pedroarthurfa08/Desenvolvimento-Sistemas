# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um outro valor dado pertence ou não à lista.

lista = [10, 25, 30, 45, 50, 60, 70, 85, 90, 100]

valor = float(input("Digite um valor para verificar se ele pertence à lista: "))

if valor in lista:
    print(f"O valor {valor} está na lista.")
else:
    print(f"O valor {valor} não está na lista.")