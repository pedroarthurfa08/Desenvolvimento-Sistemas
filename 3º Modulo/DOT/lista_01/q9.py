'''9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma. '''
def soma_intervalo(a,b):
    soma = 0
    for i in range(a,b + 1):
        soma += 1
    return soma

while True:
    try:
        n1 = int(input('\nDigite o primerio número: '))
        n2 = int(input('\nDigite o segundo número: '))

        if n1 <= n2:
            print('\nA soma do intervalo informado de é', soma_intervalo(n1, n2))
            break
        else:
            print('\nn2 deve ser maior que n1.Digite novamente!')
    except:
        print('\nAlgo de errado não está certo, tente novamente.')