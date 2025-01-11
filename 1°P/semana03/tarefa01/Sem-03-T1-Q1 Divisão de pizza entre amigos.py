'''Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre quantas fatias cada um recebe e quantas sobram.'''
# qnt_pessoas recebe o valor inteiro
qnt_pessoas = int(input("Quantas pessoas iram comer a pizza? "))
# fatias_pizza recebe o valor inteiro
fatias_pizza = int(input("São quantas fatias de pizza? "))
# fatias_recebidas recebe o valor de qnt_pessoas e será feito uma divisão (inteira) com o valor de fatias_pizza
fatias_recebidas = qnt_pessoas // fatias_pizza
# fatias_sobras recebe o valor de qnt_pessoas e será feito um módulo (resto da divisão) com o valor de fatias_pizza
fatias_sobras = qnt_pessoas % fatias_pizza
# imprimi o valor de fatias_recebidas
print(f'Então serão {fatias_recebidas} pedacos de pizza para cada pessoa.')
# imprime o valor de fatias_sobras
print(f'Caso sobre pizza, serão {fatias_sobras} fatias de pizza.')