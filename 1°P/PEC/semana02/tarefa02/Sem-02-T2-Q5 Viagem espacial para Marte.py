'''Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h. Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia.'''
# kmateM recebe um valor decimal
kmateM = float(input("Quantos quilometros (km), daqui até marte? ").strip())
# kmdanave  recebe um valor decimal
kmdanave = float(input("Quantos quilometros/hora (km/h), a sua nave espacial atinge? ").strip())
# tempmart recebe o valor de kmdanave, e será feita uma divisão (real) pelo valod e kmdanave
tempmart = kmateM / kmdanave
# imprimi o valor de tempmart
print(f'Então você deverá chegar em Marte em {tempmart} horas.')