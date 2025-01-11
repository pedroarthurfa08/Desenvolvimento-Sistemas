'''Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.'''
def main():
    poupança = 10000
    taxa_poupança = 0.007
    taxa_carro = 0.004
    preco_carro = float (input("Insira o valor do carro: "))
    meses = 0 
    while poupança < preco_carro:
        poupança += poupança * taxa_poupança
        preco_carro += preco_carro * taxa_carro
        meses += 1
    print(f"Demorará {meses} meses, para conseguir comprar o carro")
if __name__ == '__main__':
    main()