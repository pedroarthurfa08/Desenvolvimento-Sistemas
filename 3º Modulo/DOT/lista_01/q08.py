#8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um  programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os  números até o usuário responder 'N' à pergunta se ele deseja continuar ou não. 

def ler_carac():
    while True:
        caracter = input('Deseja continuar? (S/N): ')
        if caracter == 'S':
            return 'S'
        elif caracter == 'N':
            return 'N'
        else:
            print('\nCaractere inválido. Digite novamente.')


while True:
    try:
        n = float(input('Digite um número: '))
        print(f'{n} ao cubo é {n ** 3}')
        resposta = ler_carac()
        if resposta == 'N':
            break
    except ValueError:
        print('\nAlgo de errado não está certo, tente novamente.')