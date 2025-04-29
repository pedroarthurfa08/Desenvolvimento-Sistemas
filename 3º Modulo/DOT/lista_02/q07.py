# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um outro valor dado pertence ou não à lista.

def verificar_valor_na_lista(lista, valor):
    if valor in lista:
        print(f"O valor {valor} está na lista.")
    else:
        print(f"O valor {valor} não está na lista.")

lista = [10, 25, 30, 45, 50, 60, 70, 85, 90, 100]

valor = float(input("Digite um valor para verificar se ele pertence à lista: "))

verificar_valor_na_lista(lista, valor)