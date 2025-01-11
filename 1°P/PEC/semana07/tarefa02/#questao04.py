#questao04
'''
Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente:
Áries (21/03 a 19/04); Touro (20/04 a 20/05); Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07); Leão (23/07 a
22/08); Virgem (23/08 a 22/09); Libra (23/09 a 22/10); Escorpião (23/10 a 21/11); Sagitário (22/11 a 21/12);
Capricórnio (22/12 a 19/01); Aquário (20/01 a 18/02); Peixes (19/02 a 20/03);
'''
def signo(dia ,  mes ): 
    if dia >= 21 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 19 and mes == 4:
        return 'Áries'
    elif dia >= 20 and dia <= 30 and mes == 4 or dia >= 1 and dia <= 20 and mes == 5:
        return 'Touro'
    elif dia >= 21 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 21 and mes == 6:
        return 'Gêmeos'
    elif dia >= 22 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 22 and mes == 7:
        return 'Câncer'
    elif dia >= 23 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 22 and mes == 8:
        return 'Leão'
    elif dia >= 23 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
        return 'Virgem'
    elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 22 and mes == 10:
        return 'Libra'
    elif dia >= 23 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 21 and mes == 11:
        return 'Escorpião'
    elif dia >= 22 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
        return 'Sagitário'
    elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 19 and mes == 1:
        return 'Capricórnio'
    elif dia >= 20 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 18 and mes == 2:
        return 'Aquário'
    elif dia >= 19 and dia <= 29 and mes == 2 or dia >= 1 and dia <= 20 and mes == 3:
        return 'Peixes'
def main():
    dia =int(input("Insira o dia  e m que você nasceu: "))
    mes =int(input("Insira o número do mês que você nasceu: "))
    resultado=signo(dia, mes)
    print(f'Então você é do signo de {resultado}.')
if __name__ =='__main__':
    main()