#questao03
'''
Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.
'''
def calc(base, altura):
    perimetro = base * 2 + altura * 2
    area = base * altura
    if base == altura:
        return "De acordo com os dados insidos será a figura é um quadrado."
    if base != altura :
        return (f'O valor do perímetro e base do retângulo, respectivamente é {perimetro} - {area}')
def main():
    base = int(input("Insira o valor da base de uma figura geometrica: "))
    altura = int(input("Insira o valor da altura de uma figura geometrica: "))
    
    resultado = calc(base, altura)
    print(resultado)
if __name__ == '__main__':
    main()