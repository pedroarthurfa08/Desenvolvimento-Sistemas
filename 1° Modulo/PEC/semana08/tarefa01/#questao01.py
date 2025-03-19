#questao01
'''
Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de
nascimento de uma pessoa, calcule e escreva a idade exata em anos
'''
def ler(dia1, mes1, ano1, dia2, mes2, ano2):
    idade = ano1 - ano2
    if mes1 >= mes2 and dia1 >= dia2:
        return idade
    elif mes1 < mes2 and dia1 > dia2:
        return idade - 1
    elif mes1 >= mes2 and dia1 <= dia2:
        return idade - 1
    elif mes1 > mes2 and dia1 < dia2:
        return idade - 1
def main():
    dia1 = int(input("Insira o dia da data de hoje: "))
    mes1 = int(input("Insira o mês da data de hoje: "))
    ano1 = int(input("Insira o ano da data de hoje: "))
    dia2 = int(input("Insira o dia que você nasceu: "))
    mes2 = int(input("Insira o mês que você nasceu: "))
    ano2 = int(input("Insira o ano que você nasceu: "))
    resultado=ler(dia1, mes1, ano1, dia2, mes2, ano2)
    print(f'Então você tem {resultado} anos.')
if __name__=='__main__':
    main()