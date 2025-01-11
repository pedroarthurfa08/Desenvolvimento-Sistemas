#questao01
'''
Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 1 para identificar masculino e 2 para identificar feminino.
'''
def ler(nome,sexo):
    if sexo == 1:
        return 'Ilmo Sr. ' + nome
    elif sexo == 2:
        return 'Ilma Sra. ' + nome
def main():
    nome=input('Qual o seu nome? ')
    sexo=int(input("Informe seu sexo, digitando '1' caso seja masculino e '2' caso seja feminino."))
    resultado=(ler(nome,sexo))
    print(resultado)
if __name__ == '__main__':
    main()