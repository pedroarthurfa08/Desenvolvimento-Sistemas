#questao01
'''
Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os
valores lidos:
• Todos os valores são diferentes;
• Existem dois valores iguais e um diferente;
• Todos os valores são iguais.
'''
def ler(n1, n2 ,n3):
    if n1 != n2 and n1 != n3 and n2 != n3:
        return "Todos os valores são diferentes"
    elif n1 == n2 and n1 != n3:
        return "Existem dois valores iguais e um diferente"
    elif n1 == n3 and n1 != n2:
        return "Existem dois valores iguais e um diferente"
    elif n2 == n3 and n2 != n1:
        return "Existem dois valores iguais e um diferente"
    elif n1 == n2 and n1 == n3 and n2 == n3:
        return "Todos os valores são iguais"
def main():
    n1 = int(input("Insira primeiro número: "))
    n2 = int(input("Insira segundo número: "))
    n3 = int(input("Insira terceiro número: "))
    resultado = ler(n1, n2 ,n3)
    print(resultado)
if __name__ == '__main__':
    main()