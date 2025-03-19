'''Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre em quantos anos o valor acumulado será o dobro do valor inicial. Por exemplo:'''
def pop(deposito, juros):
    juros /= 100
    valor_alvo = deposito * 2
    anos = 0
    acumulado = deposito
    while acumulado < valor_alvo:
        acumulado += acumulado * juros
        anos += 1
    return anos
def main():
    deposito = float(input("Insira o valor do déposito: "))
    juros = float(input("Insira a quantidade do juros: "))
    resultado = pop(deposito, juros)
    print(f' O tempo necessário para que o valor acumulado seja o dovro do valor inicial será de {resultado} anos.')
if __name__ == '__main__':
    main()