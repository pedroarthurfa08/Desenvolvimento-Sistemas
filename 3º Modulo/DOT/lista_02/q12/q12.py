# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. Aprova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas. 

def corrigir_prova(num_alunos, gabarito, respostas):
    for aluno, resposta_aluno in respostas.items():
        acertos = 0
        for i in range(len(gabarito)):
            if resposta_aluno[i] == gabarito[i]:
                acertos += 1
        print(f'Aluno {aluno} acertou {acertos} questões.')

num_alunos = 3

gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E',
            'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E',
            'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']

respostas = {
    101: ['A', 'B', 'C', 'D', 'E'] * 6,
    102: ['A', 'B', 'C', 'D', 'E'] * 6,
    103: ['A', 'B', 'C', 'D', 'E'] * 6,
}

corrigir_prova(num_alunos, gabarito, respostas)