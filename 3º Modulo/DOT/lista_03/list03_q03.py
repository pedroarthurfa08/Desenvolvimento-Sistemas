# 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 25

def maior_soma_segmento(numeros):
    return max(numeros[i] + numeros[i + 1] for i in range(len(numeros) - 1))

# Testes
assert maior_soma_segmento([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 25
assert maior_soma_segmento([1, 2]) == 3
assert maior_soma_segmento([-1, -2]) == -3