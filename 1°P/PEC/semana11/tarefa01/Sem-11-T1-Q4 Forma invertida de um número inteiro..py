'''Escreva um programa que leia número inteiro qualquer e mostre na forma invertida'''
def invertido(x):
    numero_invertido = int(str(x)[::-1])
    return numero_invertido
def main():
    x = int(input("Insira um número: "))
    resultado = invertido(x)
    print(f'O inverso do número digitado é{resultado}')
if __name__ == '__main__':
    main()