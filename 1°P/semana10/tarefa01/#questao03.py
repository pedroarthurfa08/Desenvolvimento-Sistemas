#questao03
'''
Escreva um programa que leia um conjunto 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).
'''
def main():
    soma = 0
    for i in range (100):
        num = int(input())
        soma += num 
    media = soma / 100
    print(media)
if __name__ == '__main__':
    main()
