'''Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso contrário.'''
def eh_simbolo(caractere):
    return not caractere.isalnum()
def main():
    caractere = input("Será identificado se o caractere inserido é símbolo ou não, portanto insira um caractere: ")
    if eh_simbolo(caractere):
        print(True)
    else:
        print(False)