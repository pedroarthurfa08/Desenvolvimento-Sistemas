'''Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente.'''
# minutos recebe um valor inteiro
minutos = int(input("Digite uma quantidade de minuntos:"))
# h recebe o valor de minutos dividio (divisão inteira) por 60
h = minutos // 60
# m recebe o valor de minutos com o módulo(resto da divisão) por 60
m = minutos % 60
# imprimi o valor de minutos e quantidades de horas e minutos
print(f'A quantidade de {minutos} formatada para horas será de {h}h e {m}min.')