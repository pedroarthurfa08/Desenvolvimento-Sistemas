'''11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.'''
def valor(n):
    if n >= 0:
        return "Algo de errado, não está certo, tente novamente!"
    else:
        divisor = 0
        for i in range(1, n+1):
            if n % i == 0:
                divisor += 1
            return divisor

while True:
    try:
        n = int(input('\nDigite um número: '))
        break
    except:
        print('\nAlgo de errado não está certo, tente novamente.')