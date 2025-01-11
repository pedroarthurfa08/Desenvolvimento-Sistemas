'''Escreva um programa que leia dois valores e mostre na tela, nessa ordem:
a. A soma dos números;
b. A concatenação das strings;
c. A multiplicação dos números;
d. A multiplicação como strings;
e. A divisão dos números;
f. A divisão inteira dos números;
g. A exponenciação;
h. O módulo (resto).'''
# n1 recebe um valor real
n1 = float(input("Insira um número:"))
# n2 recebe um valor inteiro
n2 = int(input("Insira outro número:"))
# n3 recebe a string de n1
n3 = str(n1)
# n4 recebe a string de n2
n4 = str(n2)
# soma recebe o valor de n1 somado ao valor de n2
soma = n1 + n2
#
concatenacao = n3 + n4
# multiplicação rcebe o valor de n1 multiplicado a n2
multiplicacao = n1 * n2
#
multiplicação_strings = n2 * n3
# divisao recebe o valor de n1 dividido (divisão real) pelo valor de n2
divisao = n1 / n2
# divisao recebe o valor de n1 dividido (divisão interira) pelo valor de n2
divisao_inteira = n1 // n2
# exponeciacao recebe o valor de n1 elevado ao valor de n2
exponeciacao = n1 ** n2
# modulo recebe o valor de n1 realizando o módulo (resto da divisão)
modulo = n1 % n2
# imprime o valor de 
print(f'A soma destes dois números será: {soma}')
# imprime o valor de 
print(f'A concatenação destes dois números será: {concatenacao}')
# imprime o valor de 
print(f'A multiplicação destes dois números será: {multiplicacao}')
# imprime o valor de 
print(f'A multiplicação de strings destes dois números será: {multiplicação_strings}')
# imprime o valor de 
print(f'A divisão real destes dois números será: {divisao}')
# imprime o valor de 
print(f'A divisão interia destes dois números será: {divisao_inteira}')
# imprime o valor de 
print(f'A exponeciação destes dois números será: {exponeciacao}')
# imprime o valor de 
print(f'O módulo ou o resto da divisão destes dois números será: {modulo}')