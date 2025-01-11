#questao02
'''
Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou o valor booleano False (falso) caso contrário.
'''
def par(numero):
    return numero % 2
def main():
    numero = float(input("Insira um número e será identificado se tal é verdadeiro para par e falso para impar:  "))
    if par(numero)  == 1:
        print(True)
    else:
        print(False)
if __name__=='__main__':
    main()