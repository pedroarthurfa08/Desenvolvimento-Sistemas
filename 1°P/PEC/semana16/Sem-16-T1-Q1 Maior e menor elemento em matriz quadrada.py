'''Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do maior e menor elemento.'''
def ler_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

def encontrar_maior_menor(matriz):
    n = len(matriz)
    
    maior = matriz[0][0]
    menor = matriz[0][0]
    
    pos_maior = (0, 0)
    pos_menor = (0, 0)
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = (i, j)
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                pos_menor = (i, j)
    
    return pos_maior, pos_menor

n = int(input())
matriz = ler_matriz(n)

posicoes = encontrar_maior_menor(matriz)

print(f"{posicoes[0]}")
print(f"{posicoes[1]}")
