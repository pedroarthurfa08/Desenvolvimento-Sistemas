'''Você já se perguntou como seria um relógio que atrasa 3 minutos a cada hora? Vamos modelar isso com programação! Peça ao usuário para inserir o número de horas. Calcule e imprima o tempo que um relógio que atrasa 3 minutos por hora estaria atrás.'''
# nh recebe o valor de inteiro 
nh = int(input("Insira o número de horas:").strip())
# n1 recebe o valor de nh , sendo multiplicado por 3
n1 = nh * 3
# imprimi o valo de n1
print(f'O tempo de horas em minutos será de {n1} minutos.')