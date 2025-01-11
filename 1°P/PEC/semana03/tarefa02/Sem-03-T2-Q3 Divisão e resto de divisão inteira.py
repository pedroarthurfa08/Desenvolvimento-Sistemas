'''Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da divisão inteira dos valores.'''
# valor_1 recebe o valor real
valor_1 = float(input("Insira o valor do dividendo:"))
# valor_2 recebe o valor real
valor_2 = float(input("insirao valor do divisor")) 
# divisao recebe o valor_1 que será dividido (divisaõ inteira) por valor_2
divisao = valor_1 // valor_2
# resto recebe o valor_1 e será calculado o módulo(resto da divisão) por valo_2
resto = valor_1 % valor_2
# imprime o valor da divisão com 4 números deposi da vírgula
print(f'O valor do quocienta da divisão será de {divisao:.4f}')
# imprime o valor do resto com 4 números depois da vígula
print(f'O valor do quocienta da divisão será de {resto:.4f}')