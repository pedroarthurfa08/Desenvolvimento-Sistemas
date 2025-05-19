# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True caso a lista esteja ordenada em ordem ascendente ou False caso não estejaordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = FalseCódigo

def esta_ordenada(numeros):
    return all(numeros[i] <= numeros[i + 1] for i in range(len(numeros) - 1))

# Testes
numeros = [1, 2, 3]
resultado = esta_ordenada(numeros)
print(f"Lista: {numeros}")
print(f"Está ordenada: {resultado}")

numeros = [3, 7, 2]
resultado = esta_ordenada(numeros)
print(f"\nLista: {numeros}")
print(f"Está ordenada: {resultado}")

numeros = [1, 1, 2, 2, 3]
resultado = esta_ordenada(numeros)
print(f"\nLista: {numeros}")
print(f"Está ordenada: {resultado}")

numeros = []
resultado = esta_ordenada(numeros)
print(f"\nLista: {numeros}")
print(f"Está ordenada: {resultado}")

numeros = [1]
resultado = esta_ordenada(numeros)
print(f"\nLista: {numeros}")
print(f"Está ordenada: {resultado}")