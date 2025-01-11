'''Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso. IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. Por exemplo:

esta_ordenado([1, 2, 2]) True

esta_ordenado(['b', 'a']) False'''

def esta_ordenado (lista):
    return all(lista[i] <= lista[i + 1] for i in
range (len(lista) - 1) )
def main():
    n = int(input())

    lista = []
    for _ in range(n):
        valor = float(input())
        try:
            valor = float(valor)      
        except ValueError:
            pass
        lista.append(valor)
    if esta_ordenado (lista):
        print ("LISTA ORDENADA" )
    else:
        print("LISTA NÃO ORDENADA" )
if __name__ == "__main__":
    main()