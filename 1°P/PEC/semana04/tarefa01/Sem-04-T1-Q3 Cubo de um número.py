'''Escreva um programa que leia um número inteiro “x” e escreva o valor desse número elevado ao cubo.'''
# x recebe o valor interio
x = int(input("Insira um número:").strip())
# cubo recebe o valor de x elevado ao cubo, ou seja, multiplicado por 3
cubo = x ** 3
# imprime o valor do cubo
print(f'O número que será inserido elevado ao cubo é {cubo}')