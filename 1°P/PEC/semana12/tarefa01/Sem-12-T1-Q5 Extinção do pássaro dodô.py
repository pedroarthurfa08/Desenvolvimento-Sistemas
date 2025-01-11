'''O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram e o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.

Escreva um programa que leia a população de aves no início do ano 1600 e imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução quanto a população total cai para menos de 10% da população original.'''

def main():
    ano = 1600 - 1
    pop_inicial = int(input().strip())
    pop_atual = pop_inicial
    while pop_atual >= pop_inicial * 0.1:
        ano += 1
        mortes = (pop_atual * 0.06)
        nascimento = (pop_atual * 0.01)
        pop_atual = pop_atual - mortes + nascimento
        print(f'{round(ano)},{round(nascimento)},{round(mortes)},{round(pop_atual)}')
if __name__ == '__main__':
    main()