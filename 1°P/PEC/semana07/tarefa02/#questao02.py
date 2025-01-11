#questao02
'''
Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse
número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.
'''
def ler(n):
    u = n // 1% 10
    d = n // 10 % 10
    c = n // 100 % 10
    par = 0
    if n < 10:
        if u % 2 == 0:
            par = par + 1
    elif n < 100:
        if d % 2 == 0:
            par = par + 1
        if u % 2 == 0:
            par = par + 1
    elif n >= 100:
        if c % 2 == 0:
            par = par + 1
        if d % 2 == 0:
            par = par + 1
        if u % 2 == 0:
            par = par + 1
    return par
def main():
    n = int(input("Insira um número inteiro entre 100 e 999: "))
    resultado = ler(n)
    print(f'O número "{n}"tem {resultado} digítos pares.')
if __name__=='__main__':
    main()