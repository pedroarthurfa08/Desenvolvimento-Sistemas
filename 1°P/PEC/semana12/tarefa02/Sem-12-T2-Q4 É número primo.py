'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa que leia um número e determine se ele é ou não primo.'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Insira um número:; "))
if is_prime(num):
    print(f"O número {num} é True")
else:
    print(f"O número {num} é False")