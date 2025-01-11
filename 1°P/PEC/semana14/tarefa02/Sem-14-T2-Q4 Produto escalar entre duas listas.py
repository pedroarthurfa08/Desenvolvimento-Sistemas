'''Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: (x1*y1 )+(x2*y2 )+(x3*y3 )+⋯+(xn*yn). Por exemplo, para as duas listas X e Y a seguir:'''
def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        while True:
            try:
                numero = float(input())
                lista.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número real.")
    return lista

def produto_escalares(lista_x, lista_y):
    produto = 0
    expressoes = []
    for x, y in zip(lista_x, lista_y):
        produto += x * y
        expressoes.append(f"({int(x)} x {int(y)})")
    return produto, expressoes

def main():
    tamanho = 5
    
    lista_x = ler_lista(tamanho)
    lista_y = ler_lista(tamanho)
    
    produto, expressoes = produto_escalares(lista_x, lista_y)
    
    print([int(x) for x in lista_x])
    print([int(y) for y in lista_y])
    print(f"{' + '.join(expressoes)} = {int(produto)}")

if __name__ == "__main__":
    main()
