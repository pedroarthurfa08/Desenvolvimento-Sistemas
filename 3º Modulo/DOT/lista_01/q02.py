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