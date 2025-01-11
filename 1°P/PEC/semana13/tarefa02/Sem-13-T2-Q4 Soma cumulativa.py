'''Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos anteriores da lista original. IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna uma lista com a soma cumulativa. Por exemplo:
minha_lista = [1, 2, 3, 4, 5]
somacumulativa(minhalista)
[1, 3, 6, 10, 15]'''
def soma_cumulativa(lista):
    soma_acumulada = 0
    lista_cumulativa = []
    for numero in lista:
        soma_acumulada += numero
        lista_cumulativa.append(soma_acumulada)
    return lista_cumulativa
lista = []
print("Digite os números reais (digite 0 para terminar):")
while True:
    numero = float(input())
    if numero == 0:
        break
    lista.append(numero)
resultado = soma_cumulativa(lista)
print("Lista com soma cumulativa:", resultado)
