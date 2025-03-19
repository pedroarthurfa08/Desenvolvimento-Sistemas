'''Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que tem nota maior ou igual a 6 (seis).'''
notas = []
for i in range(50):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)
indices_maiores_ou_iguais_a_seis = []
for i in range(50):
    if notas[i] >= 6:
        indices_maiores_ou_iguais_a_seis.append(i)
print("Índices dos alunos com nota maior ou igual a 6:", indices_maiores_ou_iguais_a_seis)