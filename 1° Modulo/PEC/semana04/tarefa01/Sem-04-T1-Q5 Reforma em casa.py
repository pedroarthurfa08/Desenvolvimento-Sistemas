'''Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima:
• Área do piso da sala: largura * comprimento
• Volume da sala: largura * comprimento * altura
• Área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento'''
# altura recebe um valor real
altura = float(input("Insira a o valor correspondente a alura da sala:").strip())
# comprimento recebe um valor real
comprimento = float(input("Insira a o valor correspondente a comprimento da sala:").strip())
# largura recebe um valor real
largura = float(input("Insira a o valor correspondente a largura da sala:").strip())
# area_piso_sala recebe o valor de largura multiplicado ao comprimento
area_piso_sala = largura * comprimento
# volume_sala recebe o valor da largura que será multiplicado ao comprimento e depois multiplicado a altura
volume_sala = largura * comprimento * altura
# area_paredes_sala recebe o valor 2 multiplicado a altura multiplicado pela largura somado a 2 multiplicado a altura e multiplicado pelo comprimento
area_paredes_sala = 2 * altura * largura + 2 * altura * comprimento
# imprime o valor de area_piso_sala com duas casas desimais depois da virgula
print(f'A área do piso da sala será de {area_piso_sala:.2f} m².')
# imprime o valor de volume_sala com duas casas desimais depois da virgula
print(f'O volume da sala será de {volume_sala:.2f} m³.')
# imprime o valor de area_paredes_sala com duas casas desimais depois da virgula
print(f'A área das paredes da sala será de {area_paredes_sala:.2f} m².')