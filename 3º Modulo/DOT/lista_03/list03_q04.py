# 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 34

def maior_soma_seguimento(numeros):
    max_atual = max_global = numeros[0]
    for num in numeros[1:]:
        max_atual = max(num, max_atual + num)
        max_global = max(max_global, max_atual)
    return max_global

# Testes
numeros = [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]
resultado = maior_soma_seguimento(numeros)
print(f"Maior soma do seguimento: {resultado}")
assert resultado == 34, "Resultado incorreto"

numeros = [-1, -2, -3, -4]
resultado = maior_soma_seguimento(numeros)
print(f"Maior soma do seguimento: {resultado}")
assert resultado == -1, "Resultado incorreto"

numeros = [1, 2, 3, 4]
resultado = maior_soma_seguimento(numeros)
print(f"Maior soma do seguimento: {resultado}")
assert resultado == 10, "Resultado incorreto"

print("Todos os testes passaram!")