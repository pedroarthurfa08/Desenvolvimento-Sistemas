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