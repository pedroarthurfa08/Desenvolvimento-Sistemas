'''Escreva um programa que leia três números inteiros nas variáveis “a”, “b” e “c” e escreva a média deles:
• (a + b + c) / 3.'''
# n1 recebe um número inteiro
n1 = int(input("Insira um número:"))
# n2 recebe outro número inteiro
n2 = int(input("Insira outro número:"))
# n3 recebe mais um número inteiro
n3 = int(input("Insira mais um número:"))
# media recebe a soma dos valores n1, n2 e n3, depois é dividido (divisão real) por 3
media = (n1 + n2 + n3) / 3
# imprime o valor de n1, n2 e n3, junto com a média
print(f"A média dos números {n1},{n2} e {n3} é {media}")