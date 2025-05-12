# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
#o cartão de respostas para cada aluno, contendo o seu número e suas respostas.

import unittest

def corrigir_prova(gabarito, respostas_aluno):

    acertos = 0
    for i in range(len(gabarito)):
        if i < len(respostas_aluno) and gabarito[i] == respostas_aluno[i]:
            acertos += 1
    return acertos

def analisar_turma(gabarito, num_alunos, respostas_alunos):

    resultados = {}
    for numero_aluno, respostas in respostas_alunos.items():
        acertos = corrigir_prova(gabarito, respostas)
        resultados[numero_aluno] = acertos
    return resultados

class TestCorrigirProva(unittest.TestCase):
    def test_prova_totalmente_correta(self):
        gabarito = "ABCDE" * 6
        respostas = "ABCDE" * 6
        self.assertEqual(corrigir_prova(gabarito, respostas), 30)

    def test_prova_totalmente_incorreta(self):
        gabarito = "ABCDE" * 6
        respostas = "EDCBA" * 6
        self.assertEqual(corrigir_prova(gabarito, respostas), 0)

    def test_prova_parcialmente_correta(self):
        gabarito = "ABCDE" * 6
        respostas = "ABCDE" + "XXXXX" * 5
        self.assertEqual(corrigir_prova(gabarito, respostas), 5)

    def test_respostas_menor_que_gabarito(self):
        gabarito = "ABCDE" * 6
        respostas = "ABC"
        self.assertEqual(corrigir_prova(gabarito, respostas), 3)

    def test_respostas_maior_que_gabarito(self):
        gabarito = "ABC"
        respostas = "ABCDE"
        self.assertEqual(corrigir_prova(gabarito, respostas), 3)

    def test_aluno_nao_responde_nada(self):
        gabarito = "ABCDE" * 6
        respostas = ""
        self.assertEqual(corrigir_prova(gabarito, respostas), 0)

class TestAnalisarTurma(unittest.TestCase):
    def test_analisar_dois_alunos(self):
        gabarito = "ABC"
        respostas = {
            "1": "ABC",
            "2": "ABB"
        }
        resultados = analisar_turma(gabarito, 2, respostas)
        self.assertEqual(resultados, {"1": 3, "2": 2})

    def test_analisar_turma_vazia(self):
        gabarito = "ABC"
        respostas = {}
        resultados = analisar_turma(gabarito, 0, respostas)
        self.assertEqual(resultados, {})

if __name__ == "__main__":
    unittest.main()