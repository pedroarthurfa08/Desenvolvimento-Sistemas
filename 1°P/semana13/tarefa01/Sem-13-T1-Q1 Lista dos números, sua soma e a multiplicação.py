'''Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.'''
def main():
    lista = []
    soma = 0
    multi = 1
    for i in range(10):
        lista.append(int(input()))
        soma = sum(lista)
    for i in lista:
        multi *= i
    print(lista)
    print(soma)
    print(multi)
if __name__ == '__main__':
    main()