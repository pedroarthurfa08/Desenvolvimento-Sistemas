'''Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero).'''
def calcular_media():
    soma = 0
    contagem = 0
    while True:
        numero = int(input("Insira um número aleatório: "))
        if numero == 0:
            break        
        if numero > 0:
            soma += numero
            contagem += 1    
    if contagem > 0:
        media = soma / contagem
        print(f"A média entre esses números será {media:.2f}.")
if __name__ == "__main__":
    calcular_media()