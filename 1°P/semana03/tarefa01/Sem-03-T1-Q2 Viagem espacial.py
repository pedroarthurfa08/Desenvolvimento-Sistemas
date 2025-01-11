'''Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h. Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia.'''
# dst_planeta recebe um valor inteiro 
dst_planeta = int(input("Qual a distância em quilômetros do planeta no qual você desaja ir? "))
# vlc_nave recebe um valor inteiro
vlc_nave = int(input("Qual a velociade da nave no qual você deja ir? "))
# qnt_tempo recebe o valor de dst_planeta, vai ser dividido (divisão real) pelo valor de vlc_nave
qnt_tempo = dst_planeta / vlc_nave
# qnt_dias recebe qnt_tempo, vai ser dividido (divisão inteira) por 24
qnt_dias = qnt_tempo // 24
# qnt_dias recebe a forma arredondada de qnt_dias
qnt_dias = round(qnt_dias)
# qnt_horas recebe a qnt_tempo, vai ter o módulo de 24
qnt_horas = qnt_tempo % 24
#qnt_horas recebe a forma arredondada de qnt_horas
qnt_horas = round(qnt_horas)
# imprimi a qnt_dias e qnt_horas
print(f'O tempo necessário para chegar ao planeta que você deseja ir é de {qnt_dias} dias e {qnt_horas} horas.')