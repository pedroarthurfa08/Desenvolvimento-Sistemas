'''
Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

Média Final = Nota 1 + Nota 2 ∗ 2 + Nota 3 ∗ 3 + Média Exercícios
             ---------------------------------------------------
                                      7

A atribuição dos conceitos obedece a tabela abaixo.

Conceito Média Final
A >= 9.0
B >= 7.5 e < 9.0
C >= 6.0 e < 7.5
D >= 4.0 e < 6.0
E < 4.0

O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
'''
def calc_media(n1, n2, n3, media_exercicios):
    media_final = (n1 + n2 * 2 + n3 * 3 + media_exercicios) / 7
    return media_final
def main():
    matricula = input("Insira sua matrícula: ").strip()
    n1 = float(input("Insira a primeria nota: ").strip())
    n2 = float(input("Insira a segunda nota: ").strip())
    n3 = float(input("Insira a terceira nota: ").strip())
    media_exercicios = float(input("Insira a nota da média dos exercícios: ").strip())
    resultado = calc_media(n1, n2, n3, media_exercicios)
    if resultado >= 9:
        print(f'Sua matrícula é {matricula}')
        print(f'O resultado da média do exercícios será {resultado:.2f}')
        print("O conceito corresponde a: 'A'")
        print("O aluno está Aprovado")
    elif resultado >= 7.5 and resultado < 9:
        print(f'Sua matrícula é {matricula}')
        print(f'O resultado da média do exercícios será {resultado:.2f}')
        print("O conceito corresponde a: 'B'")
        print("O aluno está Aprovado")
    elif resultado >= 6 and resultado < 7.5:
        print(f'Sua matrícula é {matricula}')
        print(f'O resultado da média do exercícios será {resultado:.2f}')
        print("O conceito corresponde a: 'C'")
        print("O aluno está Aprovado")
    elif resultado >= 4 and resultado < 6:
        print(f'Sua matrícula é {matricula}')
        print(f'O resultado da média do exercícios será {resultado:.2f}')
        print("O conceito corresponde a: 'D'")
        print("O aluno está Reprovado")
    elif resultado < 4:
        print(f'Sua matrícula é {matricula}')
        print(f'O resultado da média do exercícios será {resultado:.2f}')
        print("O conceito corresponde a: 'E'")
        print("O aluno está Reprovado")
if __name__ == "__main__":
    main()