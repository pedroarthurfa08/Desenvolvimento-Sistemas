#questao02
'''
Escreva um programa que ler o valor do lado de um quadrado. Calcule o mostre a área e o perímetro desse
quadrado.
OBS: Mostre o resultado com 4 casas decimais, alinhado à direta com 10 espaços na tela.
'''
print("Esse programa lerá o valor de um quadrado e mostrará a área e perimetro desse quadrado")
def area_quadrado(lado):
    return lado * lado
def perimetro_quadrado(lado):
    return lado * 4
def main():
    lado = float(input("Insira o valor do lado do quadrado:"))
    print(f'A área do lado do quadrado será de {area_quadrado(lado)}')
    print(f'O perímetro do quadrado será de {perimetro_quadrado(lado)}')
if __name__ =='__main__':
    main()