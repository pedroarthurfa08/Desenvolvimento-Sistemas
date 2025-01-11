#questao05
'''
Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.
'''
def main():
    maior_num = 0
    for i in range(100):
        num = int(input())
        if num > maior_num:
            maior_num = num
    print(maior_num)
if __name__ == "__main__":
    main()
