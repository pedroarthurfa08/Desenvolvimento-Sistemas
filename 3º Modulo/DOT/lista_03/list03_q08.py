# 8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5

def mais_proximo_da_media(numeros):
    media = sum(numeros) / len(numeros)
    return min(numeros, key=lambda x: abs(x - media))

# Testes
numeros = [2.5, 7.5, 10.0, 4.0]
resultado = mais_proximo_da_media(numeros)
print(f"Lista: {numeros}")
print(f"Valor mais próximo da média: {resultado}")

numeros = [1, 2, 3, 4, 5]
resultado = mais_proximo_da_media(numeros)
print(f"\nLista: {numeros}")
print(f"Valor mais próximo da média: {resultado}")

numeros = [10, 20, 30]
resultado = mais_proximo_da_media(numeros)
print(f"\nLista: {numeros}")
print(f"Valor mais próximo da média: {resultado}")