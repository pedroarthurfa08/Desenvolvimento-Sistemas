'''Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_between(x, y):
    if x > y:
        x, y = y, x
    
    for num in range(x, y + 1):
        if is_prime(num):
            print(num)

x = int(input("Insira um número: "))
y = int(input("Insira outro número: "))

print_primes_between(x, y)