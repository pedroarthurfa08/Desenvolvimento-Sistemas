#questao02
'''
Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade
de números pares e números ímpares contidos no mesmo.
'''
def main():
    num_par = 0
    num_impar = 0
    for i in range (100):
        num = int(input())
        if num % 2 == 0:
            num_par += 1
        else:
            num_impar += 1
    print("Um conjunto de 100 números inteiros positivos e será determinado a quantidade de números pares.")
    print(f'A quntidade de número pares é de: {num_par}')
    print(f"A quntidade de número impares é de: {num_impar}")
if __name__ == '__main__':
    main()