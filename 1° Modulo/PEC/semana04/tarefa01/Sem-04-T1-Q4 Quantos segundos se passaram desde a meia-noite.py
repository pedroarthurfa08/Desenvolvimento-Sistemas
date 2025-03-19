'''Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a última meia-noite até a hora lida.'''
# hora rece o valor inteiro
hora = int(input("Insira uma quantidade de horas:"))
# minuto recebe o valor inteiro
minuto = int(input("Insira uma quantidade de minutos:"))
# segundo recebe um valor inteiro
segundo = int(input("Insira uma quantidade de segundos:"))
# h1 recebe o valor de hora e será multiplicado ppor 3600
h1 = hora * 3600
# m2 recebe o valor de minuto e será multiplicado por 60
m2 = minuto * 60
# total_segundos recebe o valor de h1 somado a m2 somado a segundo
total_segundos = h1 + m2 + segundo
# imprime o valor de total_segundos
print(f'A quantidade de segundos total será de {total_segundos} segundos')