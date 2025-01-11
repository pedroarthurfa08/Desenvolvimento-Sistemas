'''O tempo é algo legal, especialmente quando você vai calcular quantos minutos há em um número específico de segundos. Peça ao usuário para inserir um número de segundos. Em seguida, use a divisão inteira para mostrar esse tempo em minutos (lembre-se, 1 minuto = 60 segundos) e use o resto da divisão inteira para saber quantos segundossobram. Imprima os resultados.'''
# segundos recebe o valor inteiro
segundos = int(input("Insira uma quantidade de segundos:"))
# minutos rece o valor inteiro e será dividido (divisão inteira) por 60
minutos = segundos // 60
# segundos_sobram recebe o valo de segundos e faz o módulo (resto da divisão) do valor de 60
segundos_sobram = segundos % 60
#imprime o valor de segundos, minutos e o segundos_sobram
print(f'A quantidade de {segundos} em minutos é {minutos} e sobram {segundos_sobram} segundos.')