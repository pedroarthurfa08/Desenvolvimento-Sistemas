'''Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos (excluindo o zero).'''
def main():
    maior = None
    menor = None
    while True:
        numero = int(input("Insira um número aleatório: "))
        if numero == 0:
            break
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero
    if maior is not None and menor is not None:
        print(f"O maior número é {maior}.")
        print(f"O menor número é {menor}.")
if __name__ == '__main__':
    main()