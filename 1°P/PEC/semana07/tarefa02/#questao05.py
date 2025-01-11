#questao05
'''
Escreva um programa que leia três números e mostre na tela em ordem crescente.
'''
def ler(n1, n2, n3):
    maximo = max (n1, n2, n3)
    minimo = min (n1, n2, n3)
    if minimo < n1 and n1 < maximo:
        return (f'1- {minimo}\n2- {n1}\n3-{maximo}')
    elif minimo<n2 and n2<maximo:
        return (f'1- {minimo}\n2- {n2}\n3- {maximo}')
    elif minimo<n3 and n3>maximo:
        return (f'1- {minimo}\n2- {n3}\n3- {maximo}')
def main():
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira outro número: '))
    n3 = int(input('Insira outro número: '))
    resultado = ler(n1, n2, n3)
    print(f'A ordem do menor para o maior de {n1}, {n2} e {n3} é:')
    print(resultado)
if __name__ =='__main__':
    main()