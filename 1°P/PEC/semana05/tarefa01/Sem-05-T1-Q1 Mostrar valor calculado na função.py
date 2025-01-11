'''Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:
def calcular(a, b, c):
return 2 * a + 5 * b - c'''
# def define módulo como operação e chama para a função a, b e c
def operação(a, b, c):
    # será retornado 2 vezes o valor de a mais 5 vezes o valor de b menos c
    return 2 * a + 5 * b - c
# defini onde o programa começa
def main():
    # a recebe um número inteiro
    a = int(input("Insira um valor para a:"))
    # b recebe um número inteiro
    b = int(input("Insira um valor para b:"))
    # c recebe umnúmero inteiro
    c = int(input("Insira um valor para c:"))
    # print inprime a mensagem com o resultado da função operação
    print(f'O resultado da opereção 2 * a + 5 * b - c será {operação(a,b,c)}.')
# define como o programa termina
if __name__ =='__main__':
    main()
