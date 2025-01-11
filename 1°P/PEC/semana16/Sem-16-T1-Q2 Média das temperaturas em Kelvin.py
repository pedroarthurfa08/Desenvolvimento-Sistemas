'''Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ... ).'''
def converter_temperatura(x):
    temperatura_convertida = []
    for i in x:
        if i[1] == 'C':
            i[0] = i[0] + 273.15
            i[1] = 'K'
            temperatura_convertida.append(tuple([i[0], i[1]]))
        elif i[1] == 'F':
            i[0] = ((i[0] - 32) / 1.8) + 273.15
            i[1] = 'K'
            temperatura_convertida.append(tuple([i[0], i[1]]))
        else:
            if i[1] == 'K':
                temperatura_convertida.append(tuple([i[0], i[1]]))
    return temperatura_convertida
def media_da_temperatura(y):
    soma = 0
    score = 0
    for i in y:
        soma += i[0]
        score += 1
    media = soma / score
    return round(media, 2)
def temperatura_acima_da_media(t, m):
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    for i, x in enumerate(t):
        if x[0] > m:
            print(f'{meses[i]}: {round(x[0], 2)}K')
def main():
    l_temperatura = []
    for i in range(12):
        temperatura = float(input().strip())
        escala = str(input()).upper().strip()
        l_temperatura.append([temperatura, escala])
    r1 = converter_temperatura(l_temperatura)
    r2 = media_da_temperatura(r1)
    print(f'TEMPERATURA MÉDIA ANUAL')
    print(f'{r2}K')
    print(f'TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    temperatura_acima_da_media(r1, r2)
if __name__ == '__main__':
    main()