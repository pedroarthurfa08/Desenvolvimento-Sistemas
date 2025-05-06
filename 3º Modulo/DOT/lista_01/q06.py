#6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
#- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
#- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
#- Se o número de lados for igual a 5, escrever PENTÁGONO.
#Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

import unittest

def poligono(lado, medida_lado):
    if lado == 3:
        return f'TRIÂNGULO {(medida_lado * 3):.0f}'
    elif lado == 4:
        return f'QUADRADO {(medida_lado ** 2):.0f}'
    elif lado == 5:
        return 'PENTÁGONO'
    else:
        return 'Algo de errado não está certo, tente novamente.'

class TestPoligono(unittest.TestCase):
    def test_triangulo(self):
        self.assertEqual(poligono(3, 10), "TRIÂNGULO 30")

    def test_quadrado(self):
        self.assertEqual(poligono(4, 5), "QUADRADO 25")

    def test_pentagono(self):
        self.assertEqual(poligono(5, 7), "PENTÁGONO")

    def test_valores_invalidos(self):
        self.assertEqual(poligono(6, 10), "Algo de errado não está certo, tente novamente.")
        self.assertEqual(poligono(0, 10), "Algo de errado não está certo, tente novamente.")
        self.assertEqual(poligono(-1, 10), "Algo de errado não está certo, tente novamente.")

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            lado = int(input('\nDigite a quantidade de lados (3, 4 ou 5): '))
            if lado not in [3, 4, 5]:
                print('\nOpção inválida! Use 3, 4 ou 5.')
            else:
                medida = float(input('\nQuantos centímetros tem um lado: '))
                resultado = poligono(lado, medida)
                print(f'\nResultado: {resultado}')
                break
        except ValueError:
            print('\nAlgo de errado não está certo, tente novamente.')