# 10) Escreva uma função que recebe uma lista com n números inteiros, e determina a maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1] = 20


def maior_soma_repetidos(numeros):
    # Primeiro, conta quantas vezes cada número aparece
    contagem = {}
    for num in numeros:
        contagem[num] = contagem.get(num, 0) + 1
    
    # Calcula a soma apenas para números que aparecem mais de uma vez
    somas = {}
    for num, quantidade in contagem.items():
        if quantidade > 1:  # Só considera números que se repetem
            somas[num] = num * quantidade
    
    # Se não houver números repetidos, retorna 0
    if not somas:
        return 0
        
    return max(somas.values())

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