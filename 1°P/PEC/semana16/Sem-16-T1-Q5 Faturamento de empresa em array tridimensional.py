'''Faça um programa que leia e armazene em um array tridimensional contendo os valores do faturamento anual de uma empresa, especificados por filial e também mês a mês. Veja a estrutura do array na imagem anexa. Após a leitura dos dados faça o seguinte:

Calcule o total de cada ano por filial;
Calcule o total de todas as filiais por ano;
Calcule o total do período para todas as filiais;
Mostre todos os dados lidos e calculados de acordo com o período que ocorrer, por exemplo:'''

def ler_dados():
    dados = {}
    anos = ['2014', '2015', '2016', '2017']
    filiais = ['Filial 1', 'Filial 2', 'Filial 3']
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    for ano in anos:
        dados[ano] = {}
        for filial in filiais:
            dados[ano][filial] = []

            for mes in meses:
                venda = int(input())
                dados[ano][filial].append(venda)
                
    return dados

def calcular_totais(dados):
    totais = {}
    totais['total_geral'] = 0
    
    for ano, filiais in dados.items():
        totais[ano] = {}
        total_ano = 0
        for filial, vendas in filiais.items():
            total_filial = sum(vendas)
            totais[ano][filial] = total_filial
            total_ano += total_filial
            print(f"{ano};{filial};Janeiro;{vendas[0]}")
            for i in range(1, len(vendas)):
                print(f"{ano};{filial};{['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'][i]};{vendas[i]}")
            print(f"TOTAL {ano} {filial.upper()};{total_filial}")
        totais[ano]['total_ano'] = total_ano
        print(f"TOTAL {ano} TODAS FILIAIS;{total_ano}")
        totais['total_geral'] += total_ano
    
    print(f"TOTAL PERÍODO TODAS FILIAIS;{totais['total_geral']}")

def main():
    dados = ler_dados()
    calcular_totais(dados)

if __name__ == "__main__":
    main()
