# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True caso a lista esteja ordenada em ordem ascendente ou False caso não estejaordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = FalseCódigo

def esta_ordenada(numeros):
    return all(numeros[i] <= numeros[i + 1] for i in range(len(numeros) - 1))

# Testes
assert esta_ordenada([1, 2, 3]) == True
assert esta_ordenada([3, 7, 2]) == False
assert esta_ordenada([1, 1, 2, 2, 3]) == True
assert esta_ordenada([]) == True
assert esta_ordenada([1]) == True