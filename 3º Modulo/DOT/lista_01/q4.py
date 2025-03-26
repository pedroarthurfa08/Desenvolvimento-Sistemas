'''4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas 
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno 
foi aprovado (considere 6.0 a média mínima para aprovação).'''

def avaliacao(x1, x2):
    media = (x1 + x2) / 2
    return media >= 7, media

while True:
    try:
        x1 = float(input("\nDigite a primeira nota: "))
        x2 = float(input("\nDigite a segunda nota: "))

        aprovado, media = avaliacao(x1, x2)

        if aprovado:
            print("\n A média do aluno é %d, Parabéns!" %media)
        else:
            print("\n A média do aluno é %d, tente novamente." %media)
        break
    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")