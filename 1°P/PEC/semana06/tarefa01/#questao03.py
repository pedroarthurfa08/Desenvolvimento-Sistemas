#questao03 
'''
Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).'''
def temp(seg):
    horas = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = (seg % 3600) % 60
    return horas, minutos, segundos
def main():
    seg = int(input("Insira a duração de um evento na fábrica:"))
    horas, minutos, segundos = temp(seg)
    print(f'O evento durará {horas}:{minutos}:{segundos}')
if __name__ =='__main__':
    main()