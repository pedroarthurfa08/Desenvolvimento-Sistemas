'''Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit (baseado na fórmula abaixo): Fahrenheit = (Celsius x (9 / 5)) + 32'''
# celsius recebe umm valor real
celsius = float(input("Qual a temperatura atual em graus Celsius? ").strip())
# fahrenheitrecebe o valor de celsius multiplicado 9 dividido (divisão real) por 5 somado a 32
fahrenheit = (celsius * (9 / 5)) + 32
# imprime o valor de fahrenheit
print(f'Então a temperatura em Fahrenheit será de {fahrenheit}°')