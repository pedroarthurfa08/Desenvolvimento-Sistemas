#questao05
'''
Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.
'''
def media(nota1, nota2, nota3):
    m = (nota1+nota2+nota3)/3
    if nota3 > 8:
        m += 1
        if m > 10:
             m = 10
    return m
def main():
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terecira nota: "))
    resultado = media(nota1, nota2, nota3)
    print(f'A sua média final será {resultado:.1f}.')
if __name__=='__main__':
    main()