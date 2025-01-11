'''O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8 dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).'''
n = int(input("Insira sua data de nascimento sem a barra: "))
soma = 0
for i in range(10):
        while n > 0:
            soma += n % 10
            n //= 10
print(f'A soma dos números da sua data de nascimento é {soma}')                        