'''Escreva um programa Python que apresente o menu de opções abaixo:
OPÇÕES: 1 - SAUDAÇÃO 2 - BRONCA 3 - FELICITAÇÃO 0 - FIM
O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:
1 - Olá. Como vai? 2 - Vamos estudar mais. 3 - Meus Parabéns! 0 - Fim de serviço.
Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”. Enquanto a opção for diferente de 0 (zero) deve-se continuar apresentando as opções. Obs: use como estrutura de repetição com teste no final e como estrutura condicional múltipla escolha.'''
def main():
    while True:
        print('OPÇÕES:\n'
              '1 - SAUDAÇÃO\n'
              '2 - BRONCA\n'
              '3 - FELICITAÇÃO\n'
              '0 - FIM ')
        opcao = int(input())
        if opcao == 1 :
            print(f'{opcao} - Olá. Como vai?')
        elif opcao == 2:
            print(f'{opcao} - Vamos estudar mais.')
        elif opcao == 3:
            print(f'{opcao} - Meus Parabéns!')
        elif opcao == 0:
            print(f'{opcao} - Fim de serviço.')
            break
        else:
            print('Opção inválida.')
if __name__ == '__main__':
    main()