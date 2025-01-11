'''Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês informado. Veja o exemplo para o mês com valor 4 e 50000 para a população: CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL: Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril. Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril. Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril. Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril. ...'''
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
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    return meses.get(mes, "mês inválido")

def cidades_aniversario_e_populacao(mes, populacao, cidades):
    cidades_encontradas = [cidade for cidade in cidades if cidade[4] == mes and cidade[5] > populacao]
    if cidades_encontradas:
        print(f"CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mes_para_texto(mes).upper()}:")
        for cidade in cidades_encontradas:
            print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {mes_para_texto(mes)}.")
    else:
        print(f"Não há cidades com mais de {populacao} habitantes e aniversário em {mes_para_texto(mes).upper()}.")

def main():
    cidades = carrega_cidades()
    mes = int(input())
    populacao = int(input())
    cidades_aniversario_e_populacao(mes, populacao, cidades)

if __name__ == "__main__":
    main()
