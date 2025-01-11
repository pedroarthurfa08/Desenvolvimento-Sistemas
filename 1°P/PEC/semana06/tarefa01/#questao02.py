#questao02 
'''
Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.'''
def codigo_numerico(caractere):
    return ord(caractere)
def main():
    caractere = input("Insira um único caractere e será identificado o código númerico  correspondente ao caractere lido: ")
    resultado = (codigo_numerico(caractere))
    print(f'O caractere "{caractere}" tem o código númerioco correspondete a "{resultado}"')
if __name__=='__main__':
    main()