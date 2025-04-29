#15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)

def calculo_S(N):
    if N <= 0:
        raise ValueError("\nN dever ser um valor inteiro positivo.")
    
    S = sum((t ** 2 + 1) / (t + 3) for t in range(1, N + 1))
    return S

while True:
    try:
        N = int(input("\n Digite um número interio positivo: "))
        print("O valor de S é", calculo_S(N))
        break
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")