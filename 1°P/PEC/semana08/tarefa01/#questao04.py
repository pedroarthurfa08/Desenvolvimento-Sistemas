#questao04
'''
Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a média. Considere duas casas decimais.
'''
def calcular_media(n1, n2, n3, n4,n5) :
    media = (n1 + n2 + n3 + n4 + n5) / 5
    media_maior = [n for n in (n1,n2, n3, n4, n5) if n > media]
    return media,media_maior
def main():
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    n3 = int(input("Insira outro número: "))
    n4 = int(input("Insira outro número: "))
    n5 = int(input("Insira outro número: "))
    media, media_maior = calcular_media(n1,n2, n3, n4, n5)
    print(f'A média dos 5 números inseridos é {media: .2f}.')
    for n in media_maior:
        print(f'O número {n} é maior que a média.')
if __name__ == "__main__":
    main()