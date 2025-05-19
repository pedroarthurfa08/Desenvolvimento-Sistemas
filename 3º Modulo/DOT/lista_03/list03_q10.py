# 10) Escreva uma função que recebe uma lista com n números inteiros, e determina a maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1] = 20


def maior_soma_repetidos(numeros):
    contagem = {}
    for num in numeros:
        if num in contagem:
            contagem[num] += num
        else:
            contagem[num] = num
    return max(contagem.values())

# Testes
numeros = [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]
resultado = maior_soma_repetidos(numeros)
print(f"Lista: {numeros}")
print(f"Maior soma de números repetidos: {resultado}")

numeros = [1, 2, 2, 3, 3, 3]
resultado = maior_soma_repetidos(numeros)
print(f"\nLista: {numeros}")
print(f"Maior soma de números repetidos: {resultado}")

numeros = [-1, -1, -1, 1]
resultado = maior_soma_repetidos(numeros)
print(f"\nLista: {numeros}")
print(f"Maior soma de números repetidos: {resultado}")