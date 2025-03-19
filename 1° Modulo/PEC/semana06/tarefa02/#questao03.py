#questao03
'''
Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total! Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.'''
def maca(preco_maca):
    return preco_maca * 3
def banana(preco_banana):
    return preco_banana * 2
def total(resultado1, resultado2):
    return (resultado1 + resultado2)
def main():
    preco_maca = float(input("Insira o preço da maçã: ").strip())
    resultado1 = (maca(preco_maca))
    preco_banana = float(input("Insira o preço da banana: ").strip())
    resultado2 = (banana(preco_banana))
    print(f'O preço de três maçãs e de duas bananas será de R$ {total(resultado1, resultado2):.2f}')
if __name__ =='__main__':
    main()