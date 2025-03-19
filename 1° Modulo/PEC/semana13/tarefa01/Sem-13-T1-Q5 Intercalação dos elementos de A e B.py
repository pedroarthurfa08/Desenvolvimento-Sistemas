'''Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.'''
def main():
    A = []
    B = []

    for i in range(25):
        while True:
            try:
                numero = int (input ( ) )
                A. append (numero)
                break
            except ValueError:
                print("Por favor, digite um numero inteiro valido.")

    for i in range(25):
        while True:
                try:
                    numero = int (input())
                    B. append (numero)
                    break
                except ValueError:
                    print("Por favor, digite um numero inteiro valido.")

    C = []
    for a, b in zip(A, B) :
        C.append(a)
        C.append(b)

    print(A)
    print(B)
    print (C)

if __name__ == "__main__":
    main()