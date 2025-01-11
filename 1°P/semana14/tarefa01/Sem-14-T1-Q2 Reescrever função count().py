'''Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2 aparece na lista.
Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.'''
def ler_lista():
    lista = []
    while True:
        valor = int(input())
        if valor == 0:
            break
        lista.append(valor)
    return lista
def contar(lista, valor_pesquisar):
    count = 0
    for valor in lista:
        if valor == valor_pesquisar:
            count += 1
    return count
lista = ler_lista()
valor_pesquisar = int(input())
print(lista)
print(valor_pesquisar)
print(contar(lista, valor_pesquisar))