#questao04
'''
Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’.
Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
• para homens: (72.7 * altura) – 58
• para mulheres: (62.1 * altura) – 44.7
'''
def ler(altura, sexo):
    alt_homem = (72.7 * altura) - 58
    alt_mulher = (62.1 * altura) - 44.7
    if sexo == 1:
       return alt_homem
    elif sexo == 2:
       return alt_mulher
def main():
    altura = float(input("Insira a sua altura: "))
    sexo = float(input("Insira o seu sexo: "))
    resultado = ler(altura, sexo)
    print(f'O seu peso ideal será "{resultado:.2f}".')
if __name__=='__main__':
   main()