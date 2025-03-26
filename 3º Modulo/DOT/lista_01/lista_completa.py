"""1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar."""
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

"""2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo. Área = PI * r2; Perímetro = PI * 2 * r;"""

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

'''3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius. Fórmula: C = ((F-32)/9)*5 ''' 

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

'''4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas 
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno 
foi aprovado (considere 6.0 a média mínima para aprovação).'''

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

'''5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e 
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima).'''

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
