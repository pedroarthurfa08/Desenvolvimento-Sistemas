#questao02
'''
Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
'''
def ler(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif ano1 < ano2:
        return f'{dia2}/{mes2}/{ano2}'
    elif ano1 == ano2:
        if mes1 > mes2:
            return f'{dia1}/{mes1}/{ano1}'
        if mes1 < mes2:
            return f'{dia2}/{mes2}/{ano2}'
        elif mes1 == mes2:
            if dia1 > dia2:
                return f'{dia1}/{mes1}/{ano1}'
            if dia1 < dia2:
                return f'{dia2}/{mes2}/{ano2}'
            elif mes1 == mes2 and dia1 == dia2:
                return f'{dia1}/{mes1}/{ano1}'
def main():
    dia1 = int(input("Informe o dia de uma data: "))
    mes1 = int(input("Informe o mês de uma data: "))
    ano1 = int(input("Informe o ano de uma data: "))
    dia2 = int(input("Informe o dia de outra data: "))
    mes2 = int(input("Informe o mês de outra data: "))
    ano2 = int(input("Informe o ano de outra data: "))
    resultado=ler(dia1, mes1, ano1, dia2, mes2, ano2)
    print(f'A data mais recente é a {resultado}.')
if __name__=='__main__':
    main()