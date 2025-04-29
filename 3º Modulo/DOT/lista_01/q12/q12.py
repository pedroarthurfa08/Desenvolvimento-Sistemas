#12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
def somatorio(n):
    if n <= 0:
        raise ValueError("\nO número deve ser inteiro e positivo")
    
    somador = 0
    for i in range(1, n + 1):
        somador += i
    return somador

while True:
    try:
        num = int(input('\nDigite um número inteiro e positivo: '))
        if num > 0:
            print("\nO número digitado tem um somatório igual a ", somatorio(num))
            break
        else:
            print("\nAlgo de errado não está certo, tente novamente.")
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")