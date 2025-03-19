#questao03
'''
Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o
número lido.
• Nenhum dígito é ímpar.
• Apenas um dígito é ímpar.
• Os dois dígitos são ímpares.
'''
def ler(numero):
    dezena = numero // 10
    unidade = numero % 10
    if dezena % 2 == 0 and unidade % 2 == 0:
        return 'Nenhum dígito é ímpar.'
    elif dezena % 2 == 0 and unidade % 2 != 0 or dezena % 2 != 0 and unidade % 2 == 0:
        return 'Apenas um dígito é ímpar.'
    elif dezena % 2 != 0 and unidade % 2 != 0:
        return 'Os dois dígitos são ímpares.'
def main():
    numero = int(input())
    resultado = ler(numero)
    print(resultado)
if __name__ =='__main__':
    main()