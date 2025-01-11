#questao01
'''
Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja ímpar. Mostre na tela o resultado da operação.
'''
def ler(numero):  
    if numero % 2 == 0:
        return (f"O numero {numero} é par portanto será somado a 5 tendo como resultado: {numero + 5}.")
    elif numero % 2 != 0:
        return (f"O numero {numero} é par portanto será somado a 8 tendo como resultado: {numero + 8}.")
def main():
    numero = int(input("Insira um número intero: "))
    resultado = ler(numero)
    print(resultado)
if __name__ == '__main__':
    main()