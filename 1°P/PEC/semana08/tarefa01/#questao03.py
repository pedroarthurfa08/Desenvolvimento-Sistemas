#questao03
'''
Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes. NÃO use as funções embutidas min() e max().
'''
def lermaior(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return n2
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return n3
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return n4
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        return n5
def lermenor(n1, n2, n3, n4, n5):   
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        return n1
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        return n2
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        return n3
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        return n4
    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        return n5
def main():
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    n3 = int(input("Insira outro número: "))
    n4 = int(input("Insira outro número: "))
    n5 = int(input("Insira outro número: "))
    resultado1 = lermaior(n1, n2, n3, n4, n5)
    resultado2 = lermenor(n1, n2, n3, n4, n5)
    print(f'O maior número: {resultado1}')
    print(f'O menor número: {resultado2}')
if __name__=='__main__':
    main()