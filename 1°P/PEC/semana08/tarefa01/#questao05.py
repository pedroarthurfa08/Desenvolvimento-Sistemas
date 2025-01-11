#questao05
'''
O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:
IMC Classificação
< 18,5 Abaixo do peso
< 25 Peso normal
< 30 Sobrepeso
< 35 Obeso leve
< 40 Obeso moderado
>=40 Obeso mórbido
'''
def ler(peso, altura):
    imc = peso / altura ** 2
    print(f'O seu IMC é de {imc:.2f}')
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obeso leve'
    elif imc < 40:
        return 'Obeso moderado'
    elif imc >= 40:
        return 'Obeso mórbido'
def main():
    peso = float(input("Informe o seu peso atual: ").strip())
    altura = float(input("Informe a sua altura: ").strip())
    resultado = ler(peso, altura)
    print(f'Entção você está {resultado}.')
if __name__=='__main__':
    main()