#questao03
'''
Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
'''
def sinal(cor):
    if cor == 'V':
        return 'Siga'
    elif cor == 'A':
        return 'Atenção'
    elif cor == 'E':
        return 'Pare'
def main():
    cor = input(f'Insira para "V" para verde, "A" para amarelo e "E" para vermelho: ').upper()
    resultado = sinal(cor)
    print(resultado)
if __name__=='__main__':
    main()