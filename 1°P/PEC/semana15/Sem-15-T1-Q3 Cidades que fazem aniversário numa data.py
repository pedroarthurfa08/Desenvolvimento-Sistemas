'''Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data. Veja o exemplo para o dia 9 e mês 2: CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO: São Miguel do Passa Quatro(GO) Centralina(MG) Itaporanga(PB) ...'''
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.strip().split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    return resultado

def mes_para_texto(mes):
    meses = {
        1: "JANEIRO", 2: "FEVEREIRO", 3: "MARÇO", 4: "ABRIL",
        5: "MAIO", 6: "JUNHO", 7: "JULHO", 8: "AGOSTO",
        9: "SETEMBRO", 10: "OUTUBRO", 11: "NOVEMBRO", 12: "DEZEMBRO"
    }
    return meses.get(mes, "Mês inválido")

def cidades_aniversario(dia, mes, cidades):
    cidades_encontradas = [cidade for cidade in cidades if cidade[3] == dia and cidade[4] == mes]
    if cidades_encontradas:
        print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_para_texto(mes)}:")
        for cidade in cidades_encontradas:
            print(f"{cidade[2]}({cidade[0]})")
    else:
        print(f"Não há registros de cidades que fazem aniversário em {dia} de {mes_para_texto(mes)}.")

def main():
    cidades = carrega_cidades()
    dia = int(input())
    mes = int(input())
    cidades_aniversario(dia, mes, cidades)

if __name__ == "__main__":
    main()
