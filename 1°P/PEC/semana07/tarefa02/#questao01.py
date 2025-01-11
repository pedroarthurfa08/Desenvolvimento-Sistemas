#questao01
'''
Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. 
Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).
'''
nome=input("Insira seu nome:").strip()
estado_civil = int(input("Digite 1 caso seja casado e 2 para solteiro: ").strip())
if estado_civil == 1:
    nome_conjugue = input("Digite o nome do cônjugue: ").strip()
    a =len(nome)
    b = len(nome_conjugue)
    resultado = a + b
    print(f'Seu nome completo tem {resultado} caracteres.')
if estado_civil == 2:
    print(len(nome))