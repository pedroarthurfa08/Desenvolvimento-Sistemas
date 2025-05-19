# 9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] = [7, 3]

def eliminar_repetidos(numeros):
    contagem = {}
    for num in numeros:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1
    return [num for num, count in contagem.items() if count == 1]

# Testes
numeros = [5, 4, 5, 7, 3, 4]
resultado = eliminar_repetidos(numeros)
print(f"Lista original: {numeros}")
print(f"Lista sem repetidos: {resultado}")

numeros = [1, 2, 2, 3, 3, 3]
resultado = eliminar_repetidos(numeros)
print(f"\nLista original: {numeros}")
print(f"Lista sem repetidos: {resultado}")

numeros = [1, 1, 1, 1]
resultado = eliminar_repetidos(numeros)
print(f"\nLista original: {numeros}")
print(f"Lista sem repetidos: {resultado}")