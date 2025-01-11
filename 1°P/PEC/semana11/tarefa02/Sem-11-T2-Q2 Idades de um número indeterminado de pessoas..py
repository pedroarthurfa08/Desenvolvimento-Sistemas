'''Escreva um programa que, para um número indeterminado de pessoas:
leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada;
calcule e escreva o número de pessoas;
calcule e escreva a idade média do grupo;
calcule e escreva a menor idade e a maior idade.'''
def calcular_numeros(lista):
    numero_pessoas = len(lista)
    media = sum(lista) / numero_pessoas
    menor =min(lista)
    maior = max(lista)
    return numero_pessoas,media,menor,maior
def main():
    lista = []
    while True:
        idade = int(input("Insira a sua idade: "))
        if idade > 0:
            lista.append(idade)
        elif idade < 0:
            print()
            continue
        elif idade == 0:
            break
            continue
    numero_pessoas,media,menor,maior = calcular_numeros(lista)
    print(f' A quantidade de pessoas é {numero_pessoas}\n A média da idade de todos é {media:.2f}\n A menor idade é {menor}\n A maior idade é {maior}')
if __name__ == '__main__':
    main()
