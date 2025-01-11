'''Escreva um programa que leia o valor de um raio, calcule e mostre na tela o comprimento da circunferência, a área do círculo, a área da esfera e o volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais.'''
# importa a biblioteca math
import math
# o valor de PI é igual a 3.141592
PI = 3.141592
# raio recebe um valor real 
raio = float(input("Insira o número do raio no qual se deseja descobrir a circunferência, a área do círculo, a área da esfera e o volume da esfera:"))
# circunferencia recebe o valor de 2 multiplicado por PI e multiplicado novamente pelo raio
circunferencia = 2 * PI * raio
# imprime o valor da circunferencia com seis casas decimais depois da vírgula
print(f'Circunferencia: {circunferencia:.6f}')
# a_circulo recebe o valor de PI que será multiplicado pelo raio que será elevado a 2
a_circulo = PI * raio ** 2
# imprime o valor de a_circulo com seis casas decimais depois da virgula
print(f'Área do cículo: {a_circulo:.6f}')
# a_esfera recebe 4 que será multiplicado pelo valor de PI que multiplica pelo valor do raio que será elevadoa 2
a_esfera = 4 * PI * raio ** 2
# imprime o valor de a_esfera com seis casas decimais depois da vígula
print(f'Área da esfera: {a_esfera:.6f}')
# vol_esfera recebe 4 que será dividido (divisão rela) por 3 multiplicado pelo valor de PI multiplicado pelo valor do raio elevado a 3
vol_esfera = 4 / 3 * PI * raio ** 3
# imprime o vol_esfera com seis casas decimais depois da virgula
print(f'Volume da esfera: {vol_esfera:.6f}')