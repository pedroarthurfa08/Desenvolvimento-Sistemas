'''Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.'''
def ler_lista():
    lista = []
    for i in range(20):
        valor = int(input())
        lista.append(valor)
    return lista
def gerar_lista_soma(lista_a, lista_b):
    lista_c = []
    for i in range(20):
        lista_c.append(lista_a[i] + lista_b[i])
    return lista_c
lista_a = ler_lista()
lista_b = ler_lista()
lista_c = gerar_lista_soma(lista_a, lista_b)
print(lista_a)
print(lista_b)
print(lista_c)