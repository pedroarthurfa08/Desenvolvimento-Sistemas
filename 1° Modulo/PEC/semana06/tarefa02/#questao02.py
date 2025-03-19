#questao02
'''
Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso!
Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro
mais próximo e imprima o resultado.'''
def dinheiro(arredondar):
    return round (arredondar)
def main():
    arredondar = float(input("Insira uma quantidade de dinheiro: "))
    resultado = dinheiro(arredondar)
    print(f'O valor inteiro mais próximo de {arredondar} será {resultado}.')
if __name__=='__main__':
    main()