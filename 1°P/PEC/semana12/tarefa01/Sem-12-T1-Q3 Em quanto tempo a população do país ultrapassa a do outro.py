'''Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a população do país A.'''
def calcular_tempo_ultrapassar(pop_a, taxa_a, pop_b, taxa_b):
    anos = 0
    while pop_b <= pop_a:
        pop_a *= (1 + taxa_a)
        pop_b *= (1 + taxa_b)
        anos += 1
    return anos
def main():
    tx_crescimento_a = 0.02
    tx_crescimento_b = 0.03

    pop_1 = float(input("Insira o valor da população do país a:"))
    pop_2 = float(input("Insira o valor da população do país b:"))

    if pop_1 > pop_2:
        pop_a = pop_1
        pop_b = pop_2
    else:
        pop_a = pop_2
        pop_b = pop_1
    anos = calcular_tempo_ultrapassar(pop_a, tx_crescimento_a, pop_b, tx_crescimento_b)

    print(f'O tempo necessário para que a população do país B ultrapasse a população do país A é de {anos} anos.')
if __name__ == "__main__":
    main()