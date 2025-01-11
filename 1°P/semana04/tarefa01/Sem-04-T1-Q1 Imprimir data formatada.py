'''Considere que as variáveis “dia”, “mês” e “ano” contém os valores respectivos de uma certa data. Escreva um comando “print” que imprima essa data no formato usado, por exemplo, “15/4/2020” ou “2/12/2004”.'''
# dia recebe o valor inteiro
dia = int(input("Insira o dia que você deseja colocar na data formatada:"))
# mês recebe o valor inteiro
mes = int(input("Insira o mês que você deseja colocar na data formatada:"))
# ano recebe o valor inteiro
ano = int(input("Insira o ano que você deseja colocar na data formatada:"))
# imprime o valor de dia, mês e ano formatado para data
print(f'{dia}/{mes}/{ano}')