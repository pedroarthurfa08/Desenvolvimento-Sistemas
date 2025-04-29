#13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N

def calculo_S(N):
    if N <= 0:
        raise ValueError("\nN dever ser um valor inteiro positivo.")
    
    S = sum(1 / i for i in range(1, N + 1))
    return S

while True:
    try:
        N = int(input("\n Digite um número interio positivo: "))
        print("O valor de S é", calculo_S(N))
        break
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")