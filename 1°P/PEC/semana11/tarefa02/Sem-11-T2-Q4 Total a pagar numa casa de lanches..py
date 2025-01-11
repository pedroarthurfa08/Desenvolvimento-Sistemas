'''Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.” caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar uma nota válida, o aluno deve ver seu conceito, segundo a tabela:'''
def main():
    total = 0
    while True:
        print('CÓDIGO  PRODUTO         PREÇO (R$)\n'
              'H       Hamburger       5,50\n'
              'C       Cheeseburger    6,80\n'
              'M       Misto Quente    4,50\n'
              'A       Americano       7,00\n'
              'Q       Queijo Prato    4,00\n'
              'X       PARA TOTAL DA CONTA')
        opcao = str(input()).strip().upper()
        if opcao == 'H':
            total += 5.50
        elif opcao == 'C' :
            total += 6.80
        elif opcao == 'M':
            total += 4.50
        elif opcao == 'A':
            total += 7.00
        elif opcao == 'Q':
            total += 4.00
        elif opcao == 'X':
            break
        else:
            print('Opção inválida.')
    print(f'{total:.2f}')
if __name__ == '__main__':
    main()