#questao02
'''
Escreva um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da
seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa
operação sobre os dois valores lidos.
'''
def calc(n1, n2, operacao):
    if operacao == 1:
       return n1 + n2 
    elif operacao == 2:
       return n1 - n2 
    elif operacao == 3:
       return n1 * n2 
    elif operacao == 4:
       return n1 / n2 
def main():
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))
    operacao = int(input("Insira um desses números para determinar a operação 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão: "))
    resultado = calc(n1, n2, operacao)
    print(f'O resultado da operação solicitada será {resultado}')
if __name__ == '__main__':
    main()