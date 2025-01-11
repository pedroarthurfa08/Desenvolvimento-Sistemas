#questao04
'''
Um sacolão está vendendo frutas com a seguinte tabela de preços:

Até 5Kg Acima de 5Kg
Morango - R$ 2,50 por Kg - R$ 2,20 por Kg
Maça -  R$ 1,80 por Kg - R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
def main():
    morango_kg = float(input("Quantos quilos de morango você levando? "))
    maca_kg = float(input("Quantos quilos de macã você levando? "))

    preco_morango = 2.50 if morango_kg <= 5 else 2.20
    preco_maca = 1.80 if maca_kg <= 5 else 1.50

    total_sem_desconto = (morango_kg * preco_morango) + (maca_kg * preco_maca)

    if (morango_kg + maca_kg) > 8 or total_sem_desconto > 25:
        total_com_desconto = total_sem_desconto * 0.9
    else:
        total_com_desconto = total_sem_desconto

    print(f"Então no final o preço do seu sacolão será de {total_com_desconto:.2f} reais.")
if __name__ == "__main__":
    main()