#7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro.

def fatorial(f):
    fat = 1
    for i in range(1, f + 1):
        fat = fat * i
    return fat

while True:
    try:
        num = int (input("\nDigite um número:"))
        print("\nO fatorial de %d é: %d" %(num, fatorial(num)))
        break
    except:
        print("\nAlgo de errado não está certo, tente novamente.")