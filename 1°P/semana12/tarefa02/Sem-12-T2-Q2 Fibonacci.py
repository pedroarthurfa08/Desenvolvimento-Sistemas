'''A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre será maior ou igual a 2.'''
def fibonacci(x):
    ultimo = 1
    penultimo = 0
    valor = '0, 1'
    for i in range(2, x):
        prox_num = ultimo + penultimo
        valor += f', {prox_num}'
        penultimo = ultimo
        ultimo = prox_num
    return valor
def main():
    n = int(input().strip())
    resultado = fibonacci(n)
    print(f'{resultado}')
if __name__ == '__main__':
    main()