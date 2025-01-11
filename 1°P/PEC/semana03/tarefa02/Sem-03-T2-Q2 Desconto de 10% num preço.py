'''Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado para duas casas decimais.'''
# preço recebe um valor real
preço = float(input("Insira o preço a ser descontado:"))
# preço_desconto recebe o valor de preço multiplicado por 0.90
preço_desconto = preço * 0.90
# preço_desconto será arredondado
preço_desconto = round(preço_desconto,2 )
# imprime o valor do preço_desconto
print(f'O valor do desconto será de {preço_desconto} reias.')