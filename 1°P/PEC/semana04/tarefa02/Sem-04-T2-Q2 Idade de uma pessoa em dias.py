'''Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. Considerar sempre os anos com 365 dias e os messes com 30 dias'''
# anos recebe um valor de inteiro
anos = int(input("Quantos anos você tem?"))
# meses recebe o valor inteiro 
meses = int(input("Quantos meses de vida você tem depois que completou ano?"))
# dias recebe um valor inteiro  
dias = int(input("Quantos dias desde o seu útimos mêsversário?"))
# anos 1 recebe o valor de anos que será multiplicado por 365
anos1 = anos * 365
# meses1 recebe o valor de meses multiplicado por 365
meses1 = meses * 30
# dias_totais revebe o valor de anos 1 mais o valor de meses1 mais a quantidade de dias
dias_totais = anos1 + meses1 + dias
# imprime o valor de dias_totais
print(f'Então você tem exatamente {dias_totais} dias de vida.')