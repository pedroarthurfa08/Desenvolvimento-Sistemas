# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V aparece. Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.

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

def contar_ocorrencias(lista, valor):
    indices = []
    for i in range(len(lista)):
        if lista[i] == valor:
            indices.append(i)
        return indices

def exibir_resultado(indices, valor):
    if indices:
        print(f"\nO valor {valor} ocorre {len(indices)} vezes na lista.")
        print("Ele aparece nas posições:", indices)
    else:
        print(f"\nO valor {valor} **não aparece** na lista.")

def main():
    W = ler_lista(10)
    while True:
        try:
            V = int(input("\nDigite o valor a ser buscado na lista: "))
            break
        except ValueError:
            print("Digite um número inteiro.")
    
    ocorrencias = contar_ocorrencias(W, V)
    exibir_resultado(ocorrencias, V)

main()