# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

def inverter_lista(lista):
    lista_invertida = lista[::-1]
    print("Lista x:", lista)
    print("Lista y (invertida):", lista_invertida)