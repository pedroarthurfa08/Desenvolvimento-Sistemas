'''Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1'''
n = int(input("Insira um número para calcular a fatorial"))
fatorial = 1
for i in range(1, n +1):
    fatorial *= i
print(f'O valor de {n} fatorial é {fatorial}')