#questao04
'''
Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.'''
def converter(ano):
    return ano // 2
def main():
    ano = int(input("Para descobrir quantos anos espaciais você tem, insira sua idade atual: "))
    qnt_ano = (f"{converter(ano):.0f}")
    print(f'Se você tem {ano} anos, em anos espaciais você terá {qnt_ano} anos.')
if __name__ =='__main__':
    main()