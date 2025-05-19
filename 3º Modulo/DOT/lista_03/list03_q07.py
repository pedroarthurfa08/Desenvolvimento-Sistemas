# 7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True caso algum elemento apareça mais de uma vez ou False caso nenhum elemento apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

def tem_repeticoes(numeros):
    return len(numeros) != len(set(numeros))

# Testes
numeros = [1, 2, 3, 1]
resultado = tem_repeticoes(numeros)
print(f"Lista: {numeros}")
print(f"Tem repetições: {resultado}")

numeros = [3, 7, 2, 4]
resultado = tem_repeticoes(numeros)
print(f"\nLista: {numeros}")
print(f"Tem repetições: {resultado}")

numeros = [1, 1, 1, 1]
resultado = tem_repeticoes(numeros)
print(f"\nLista: {numeros}")
print(f"Tem repetições: {resultado}")

numeros = []
resultado = tem_repeticoes(numeros)
print(f"\nLista: {numeros}")
print(f"Tem repetições: {resultado}")

numeros = [1]
resultado = tem_repeticoes(numeros)
print(f"\nLista: {numeros}")
print(f"Tem repetições: {resultado}")