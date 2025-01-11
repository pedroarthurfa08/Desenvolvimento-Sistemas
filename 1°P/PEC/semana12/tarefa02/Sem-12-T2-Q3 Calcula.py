'''Calcular H =1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o valor de H com 4 (quatro) casas decimais. O número n é lido.'''
def calcular_harmonico(n):
    H = 0.0
    for i in range(1, n + 1):
        H += 1 / i
    return H
n = int(input("Insira um valor: "))
H = calcular_harmonico(n)
print(f"O número {n} lido é {H:.4f}")