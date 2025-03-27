#1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def par_impar(x):
    if x % 2 == 0:
        return True
    else: 
        return False

while True:
    try:  
        num = int(input("\nDigite um número: "))
        if par_impar(num):
            print("\nO número %d é par." %num)
        else:
            print("\nO número %d é ímpar." %num)
        break
    except:
        print("\nAlgo de errado não está certo, tente novamente.")

#======================================================================================================================================================================================

#2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo. Área = PI * r2; Perímetro = PI * 2 * r;

def area(r):
    return 3.14 * r ** 2
def perimetro(r):
    p = 3.14 * 2 * r
    return p

while True:
    try:
        r = float(input("Digite o valor do raio: "))
        print("\nA área do cículo é %2f" % area(r))
        print("\no perímetro do cículo é %2f" % perimetro(r))
        break
    except:
        print("\nAlgo de errado não está certo, tente novamente.")

#======================================================================================================================================================================================

#3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius. Fórmula: C = ((F-32)/9)*5

def celsius(f):
    return ((f-32)/9)*5

while True:
    try:
        f = float(input("Digite a temperatura em Celsius: "))
        print("\no perímetro do cículo é %2f" % celsius(f))
        break
    except:
        print("\nAlgo de errado não está certo, tente novamente.")

#======================================================================================================================================================================================

#4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas  notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def avaliacao(x1, x2):
    media = (x1 + x2) / 2
    return media >= 7, media

while True:
    try:
        x1 = float(input("\nDigite a primeira nota: "))
        x2 = float(input("\nDigite a segunda nota: "))

        aprovado, media = avaliacao(x1, x2)

        if aprovado:
            print("\n A média do aluno é %d, Parabéns!" %media)
        else:
            print("\n A média do aluno é %d, tente novamente." %media)
        break
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")

#======================================================================================================================================================================================

#5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
#1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
#- para homens : (72.7 * h) – 58
#- para mulheres : (62.1 * h) – 44.7
#Observação: Altura = h (na fórmula acima).

def altura(h, sexo):
    if sexo == 1:
        return (62.1 * h) - 44.7
    elif sexo == 2:
        return (72.7 * h) - 58
    else:
        return None

for _ in range(1):
    try:
        sexo = int(input("\nDigite seu 1 para mulher e 2 para homem: "))
        if sexo not in[1, 2]:
            print("\nOpção Inválida!")
            break

        h = float(input("\nInforme sua altura em metros: "))
        print("\nSeu peso ideal é: %.2f kg" %altura(h, sexo))

    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")

#======================================================================================================================================================================================

#6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
#- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
#- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
#- Se o número de lados for igual a 5, escrever PENTÁGONO.
#Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

def poligono(lado, medida_lado):
    if lado == 3:
        triangulo = medida_lado *3
        return f'TRIÂNGULO {triangulo:.0f}'
    elif lado == 4:
        quadrado = medida_lado ** 2
        return f'QUADRADO {quadrado:.0f}'
    elif lado == 5:
        return f'PENTÁGONO'
    else:
        return f'Algo de errado não está certo, tente novamente.'

while True:
    try:
        lado = int(input('\nDigite a quantidade de lados: '))
        medida_lado = float(input('\nQuantos centímetros tem um lado: '))
        if lado > 0 and medida_lado > 0:
            print(poligono(lado, medida_lado))
            break
    except:
        print('Algo de errado não está certo, tente novamente.')

#======================================================================================================================================================================================

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

#======================================================================================================================================================================================

#8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um  programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os  números até o usuário responder 'N' à pergunta se ele deseja continuar ou não. 

def ler_carac():
    while True:
        caracter = input('Deseja continuar? (S/N): ')
        if caracter == 'S':
            return 'S'
        elif caracter == 'N':
            return 'N'
        else:
            print('\nCaractere inválido. Digite novamente.')


while True:
    try:
        n = float(input('Digite um número: '))
        print(f'{n} ao cubo é {n ** 3}')
        resposta = ler_carac()
        if resposta == 'N':
            break
    except ValueError:
        print('\nAlgo de errado não está certo, tente novamente.')

#======================================================================================================================================================================================

#9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
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

#======================================================================================================================================================================================

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

#======================================================================================================================================================================================

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

#======================================================================================================================================================================================

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

#======================================================================================================================================================================================

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

#======================================================================================================================================================================================

#14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + 1/1! + ½! + 1/3! + 1 /N!

import math

def calculo_S(N):
    if N <= 0:
        raise ValueError("\nN dever ser um valor inteiro positivo.")
    
    S = sum(1 / math.factorial(i) for i in range(1, N + 1))
    return S

while True:
    try:
        N = int(input("\n Digite um número interio positivo: "))
        print("O valor de S é", calculo_S(N))
        break
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")

#======================================================================================================================================================================================

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
