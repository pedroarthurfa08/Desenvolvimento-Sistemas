#questao 04 
'''
Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
• o maior número lido;
• o menor número lido;
• a média aritmética dos números lidos.
'''
def maior(n1,n2,n3,n4,n5):
    return max (n1,n2,n3,n4,n5)
def menor(n1,n2,n3,n4,n5):
    return min (n1,n2,n3,n4,n5)
def media(n1,n2,n3,n4,n5):
    return (n1+n2+n3+n4+n5) / 5
def main():
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    n3 = int(input("Insira outro número: "))
    n4 = int(input("Insira outro número: "))
    n5 = int(input("Insira outro número: "))
    rslt_menor = (menor(n1,n2,n3,n4,n5))
    rslt_media = (media(n1,n2,n3,n4,n5))
    rslt_maior = (maior(n1,n2,n3,n4,n5))
    print(f'O maior número da sequência é {rslt_maior}')
    print(f'O menor número da sequência é {rslt_menor}')
    print(f'A média entre os número da sequência é{rslt_media}')
if __name__=='__main__':
    main()