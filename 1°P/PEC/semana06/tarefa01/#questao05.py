#questao05
'''
Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:
• Valor para pagamento à vista, com desconto de 9%.
• Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
• Valor da prestação para pagamento em 10 vezes, com 17% de juros.
'''
def desconto(preco):
    return preco - (preco * 0.09)
def prest_5_semjuros(preco):
    return preco / 5
def prest_10_comjuros(preco):
    op1 = preco / 10
    op2 = (preco * 0.17) / 10
    return op1 + op2
def main():
    preco = float(input("Insira o valor da peça de roupa: "))
    resultado1 = (desconto(preco))
    resultado2 = (prest_5_semjuros(preco))
    resultado3 = (prest_10_comjuros(preco))
    print(f'Com o pagamento à vista, terá um desconto de 9% e o valor da peça ficará: {resultado1:.2f}')
    print(f'O pagamento em 5 vezes, sem desconto nem juros ficará: {resultado2:.2f}')
    print(f'O pagamento em 10 vezes, com 17% de juros, ficará: {resultado3:.2f}')
if __name__ =='__main__':
    main()