'''Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação: A condição de saída do laço será a leitura do valor 0 (flag).'''
soma = 0
while True:
    numero = int(input("Insira um número: "))
    if numero == 0:
        break
    soma += numero
print(f'A soma de todos os número inseridos será {soma}.')