# 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma lista com a soma cumulativa dos elementos da lista original onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] = [1,3,6]

def soma_cumulativa(numeros):
    soma = 0
    resultado = []
    for num in numeros:
        soma += num
        resultado.append(soma)
    return resultado

# Testes
assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]
assert soma_cumulativa([-1, 1, -1, 1]) == [-1, 0, -1, 0]
assert soma_cumulativa([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]