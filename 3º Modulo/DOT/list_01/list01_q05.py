# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
#1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
#- para homens : (72.7 * h) – 58
#- para mulheres : (62.1 * h) – 44.7
#Observação: Altura = h (na fórmula acima).

import unittest

def peso_ideal(h, sexo):
    if sexo == 1:
        return (62.1 * h) - 44.7
    elif sexo == 2:
        return (72.7 * h) - 58
    else:
        return None

class TestPesoIdeal(unittest.TestCase):
    def test_mulher(self):
        self.assertAlmostEqual(peso_ideal(1.60, 1), (62.1 * 1.60) - 44.7)

    def test_homem(self):
        self.assertAlmostEqual(peso_ideal(1.75, 2), (72.7 * 1.75) - 58)

    def test_sexo_invalido(self):
        self.assertIsNone(peso_ideal(1.75, 3))

if __name__ == '__main__':
    unittest.main(exit=False)

'''import unittest

def peso_ideal(h, sexo):
    if sexo == 1:
        return (62.1 * h) - 44.7
    elif sexo == 2:
        return (72.7 * h) - 58
    else:
        return None

class TestPesoIdeal(unittest.TestCase):
    def test_mulher(self):
        self.assertAlmostEqual(peso_ideal(1.60, 1), (62.1 * 1.60) - 44.7)

    def test_homem(self):
        self.assertAlmostEqual(peso_ideal(1.75, 2), (72.7 * 1.75) - 58)

    def test_sexo_invalido(self):
        self.assertIsNone(peso_ideal(1.75, 3))

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            sexo = int(input("\nDigite 1 para mulher ou 2 para homem: "))
            if sexo not in [1, 2]:
                print("\nOpção inválida! Use 1 para mulher e 2 para homem.")
            else:
                h = float(input("\nInforme a altura em metros (ex: 1.70): "))
                peso = peso_ideal(h, sexo)
                print(f"\nSeu peso ideal é: {peso:.2f} kg")
                break
        except ValueError:
            print("\nAlgo de errado não está certo, tente novamente.")'''