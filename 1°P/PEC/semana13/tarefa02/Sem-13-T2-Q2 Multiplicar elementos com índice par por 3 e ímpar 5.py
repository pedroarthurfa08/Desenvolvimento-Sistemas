'''Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5. DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.'''
numeros = []
for _ in range(100):
    num = int(input("Digite um número: "))
    numeros.append(num)
numeros_ordenados = sorted(numeros)
nova_lista = [
    num * 3 if i % 2 == 0 else num * 5
    for i, num in enumerate(numeros_ordenados)
]
print("Lista final modificada:", nova_lista)
