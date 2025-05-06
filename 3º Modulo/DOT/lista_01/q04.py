# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas  notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

import unittest

def avaliacao(x1, x2):
    media = (x1 + x2) / 2
    aprovado = media >= 6
    return aprovado, media

class TestAvaliador(unittest.TestCase):
    def test_aprovado(self):
        aprovado, media = avaliacao(7, 8)
        self.assertTrue(aprovado)
        self.assertEqual(media, 7.5)

    def test_reprovado(self):
        aprovado, media = avaliacao(5, 5)
        self.assertFalse(aprovado)
        self.assertEqual(media, 5.0)

    def test_limiar(self):
        aprovado, media = avaliacao(6, 6)
        self.assertTrue(aprovado)
        self.assertEqual(media, 6.0)

    def test_notas_negativas(self):
        aprovado, media = avaliacao(-2, -3)
        self.assertFalse(aprovado)
        self.assertEqual(media, -2.5)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            x1 = float(input("\nDigite a primeira nota: "))
            x2 = float(input("\nDigite a segunda nota: "))
            aprovado, media = avaliacao(x1, x2)
            if aprovado:
                print(f"\nA média do aluno é {media:.2f}. PARABÉNS! Você foi aprovado!")
            else:
                print(f"\nA média do aluno é {media:.2f}. Tente novamente.")
            break
        except ValueError:
            print("\nAlgo de errado não está certo, tente novamente.")