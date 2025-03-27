#10. Escreva um programa composto de uma função Max e o programa principal como segue:
#a) A função Max recebe como parâmetros de entrada 4  números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
#b) O programa principal lê 4 séries de 4 números a, b, c, d Para cada série lida imprime o maior dos quatro números usando a função Max.

def Max(a, b, c, d):
    return max(a, b, c, d)

while True:
    try:
        for i in range(4):
            print(f"Série {i+1}:")
            
            a = int(input("Digite o número a: "))
            b = int(input("Digite o número b: "))
            c = int(input("Digite o número c: "))
            d = int(input("Digite o número d: "))
            
            maior = Max(a, b, c, d)
            print(f"O maior número é: {maior}\n")
        break
    except ValueError:
        ('\nAlgo de errado não está certo, tente novamente.')