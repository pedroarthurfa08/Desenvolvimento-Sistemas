#16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.

def ler_lista(tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros e positivos: ")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"Elemento {i}: "))
                if num > 0:
                    lista.append(num)
                    break
                else:
                    print("O número deve ser positivo.")
            except ValueError:
                print("Resposta inválida, digite um número inteiro.")
    return lista

def transformar_lista(lista_x):
    lista_y = []
    for i in range(len(lista_x)):
        if i % 2 == 0:
            lista_y.append(lista_x[i] / 2)
        else:
            lista_y.append(lista_x[i] * 3)
    return lista_y

def exibir_listas(lista_x, lista_y):
    print("\nLista X:", lista_x)
    print("Lista Y:", lista_y)

def main():
    X = ler_lista(10)
    Y = transformar_lista(X)
    exibir_listas(X, Y)

main()