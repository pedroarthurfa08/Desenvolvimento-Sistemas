#11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
def contar_divisores(n):
    if n <= 0:
        raise ValueError("\nO número deve ser inteiro e positivo.")
    
    divisor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor += 1
    return divisor

while True:
    try:
        num = int(input("\nDigite um número inteiro e positivo: "))
        if num > 0:
            print("\nO número digitado tem", contar_divisores(num), "divisores.")
            break
        else:
            print("\nAlgo de errado não está certo, tente novamente.")
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")