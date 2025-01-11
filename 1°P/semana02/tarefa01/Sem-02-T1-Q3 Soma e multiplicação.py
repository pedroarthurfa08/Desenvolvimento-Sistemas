''''Escreva um programa que leia dois números e mostre na tela a soma e a multiplicação deles.'''
# n1 recebe um valor inteiro
n1 = int(input("Insira um número:"))
# n2 recebe um valor inteiro
n2 = int(input("Insira outro número:"))
# soma recebe o valor de n1 e será somando ao valor de n2
soma = n1 + n2
# multiplicação recebe o valor de n1 e será multiplicado ao valor de n2
multiplicacao = n1 * n2
# imprimi o valor da soma
print(f'A soma de {n1} com {n2} é igual a {soma}')
# imprime o valor da multiplicação
print(f'A multiplicação de {n1} com {n2} é igual a {multiplicacao}')