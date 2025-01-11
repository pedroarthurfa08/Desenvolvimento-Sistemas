#questao04
'''
Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertida
de para horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.
OBS: Mostre o resultado na forma H:M
'''
print("Colocando os minutos em formato de hora.")
def horas(min):
    return min // 60
def minutos(min):
    return min % 60
def main():
    min=int(input("Insira a quantidade de minutos que será tranformada em formato de horas:"))
    print(f'Tranformando {min} em formato de horas ficará {horas(min)}:{minutos(min)}')
if __name__ =='__main__':
    main()