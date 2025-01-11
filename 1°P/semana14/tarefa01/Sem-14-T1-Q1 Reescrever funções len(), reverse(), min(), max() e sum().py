'''As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
a) len(), que recebe uma lista e retorna número de itens; b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida; c) min(),que recebe uma lista e retorna o menor valor d) max(), que recebe uma lista retorna o maior valor e) sum(), que recebe uma lista retorna a soma dos valores
Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o resultado encontrado.
Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), minimo(), maximo(), soma().
'''
def ler_lista():
    lista = []
    while True:
        valor = int(input())
        if valor == 0:
            break
        lista.append(valor)
    return lista
def comprimento(lista):
    count = 0
    for _ in lista:
        count += 1
    return count
def inverter(lista):
    lista_invertida = []
    for i in range(comprimento(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida
def minimo(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor
def maximo(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior
def soma(lista):
    total = 0
    for valor in lista:
        total += valor
    return total
lista = ler_lista()
print(lista)
print(comprimento(lista))
print(inverter(lista))
print(minimo(lista))
print(maximo(lista))
print(soma(lista))