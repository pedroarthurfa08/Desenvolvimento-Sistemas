'''Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente: a) a soma dos elementos da primeira linha b) a soma dos elementos da última coluna c) a média de todos os elementos d) o menor elemento e) o maior elemento'''
def ler_matriz(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

def soma_primeira_linha(matriz):
    return sum(matriz[0])

def soma_ultima_coluna(matriz):
    return sum(linha[-1] for linha in matriz)

def media_elementos(matriz):
    total_elementos = sum(len(linha) for linha in matriz)
    soma_total = sum(sum(linha) for linha in matriz)
    return soma_total / total_elementos

def menor_elemento(matriz):
    return min(min(linha) for linha in matriz)

def maior_elemento(matriz):
    return max(max(linha) for linha in matriz)

def main():
    n = int(input())
    m = int(input())
    
    matriz = ler_matriz(n, m)
    
    soma_primeira = soma_primeira_linha(matriz)
    soma_ultima = soma_ultima_coluna(matriz)
    media = media_elementos(matriz)
    menor = menor_elemento(matriz)
    maior = maior_elemento(matriz)
    
    resultado = (soma_primeira, soma_ultima, round(media, 4), menor, maior)
    print(resultado)

if __name__ == "__main__":
    main()
