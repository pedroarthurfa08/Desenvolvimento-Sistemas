# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

def ler_lista(tamanho):
    lista = []
    print(f"Digite {tamanho} números inteiros (positivos ou negativos):")
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"Elemento {i}: "))
                lista.append(num)
                break
            except ValueError:
                print("Resposta inválida, digite um número inteiro.")
    return lista

def filtrar_negativos(lista):
    negativos = [num for num in lista if num < 0]
    return negativos

def exibir_lista(lista_x, lista_r):
    print("\nLista X:", lista_x)
    print("Lista R (somente negativos):", lista_r)

def main():
    X = ler_lista(10)
    R = filtrar_negativos(X)
    exibir_lista(X, R)

main()