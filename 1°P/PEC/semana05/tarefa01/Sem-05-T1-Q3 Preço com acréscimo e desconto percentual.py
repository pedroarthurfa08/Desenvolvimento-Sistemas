#questao03
'''
Escreva um programa que leia um preço e um valor percentual. Informe o preço acrescido do percentual e o
preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e um valor percentual de 5.00 o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.
OBS: Mostre sempre duas casas decimais.
'''
print("Esse código irá mostra o acréscimo e o desconto de um valor, de acordo com porcentagem informada.")
def acrescimo(preco, porcentagem):
    return preco + (preco * porcentagem / 100)
def desconto(preco, porcentagem):  
    return preco - (preco * porcentagem / 100)
def main():
    preco=float(input("Insira o preço:").strip())
    porcentagem=float(input("Insira a porcentagem na qual será aumentada ou descontada do valor:").strip())
    print(f'O valor com acréscimo será de R$ {acrescimo(preco, porcentagem):.2f}')
    print(f'O valor com desconto será de R$ {desconto(preco, porcentagem):.2f}')
if __name__ =='__main__':
    main()