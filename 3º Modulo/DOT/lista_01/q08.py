# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um  programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os  números até o usuário responder 'N' à pergunta se ele deseja continuar ou não. 

import unittest

def ler_carac(input_func=input):
    while True:
        caracter = input_func('Deseja continuar? (S/N): ').strip().upper()
        if caracter == 'S':
            return 'S'
        elif caracter == 'N':
            return 'N'
        else:
            print('\nCaractere inválido. Digite novamente.')

def ao_cubo(n):
    return n ** 3

class TestCuboEEntrada(unittest.TestCase):
    def test_ao_cubo_positivo(self):
        self.assertEqual(ao_cubo(3), 27)

    def test_ao_cubo_zero(self):
        self.assertEqual(ao_cubo(0), 0)

    def test_ao_cubo_negativo(self):
        self.assertEqual(ao_cubo(-2), -8)

    def test_ler_carac_s(self):
        self.assertEqual(ler_carac(lambda _: 'S'), 'S')

    def test_ler_carac_n(self):
        self.assertEqual(ler_carac(lambda _: 'N'), 'N')

    def test_ler_carac_invalido_then_s(self):
        inputs = iter(['x', 'S'])
        self.assertEqual(ler_carac(lambda _: next(inputs)), 'S')

if __name__ == '__main__':
    unittest.main(exit=False)

'''import unittest

def ler_carac(input_func=input):
    while True:
        caracter = input_func('Deseja continuar? (S/N): ').strip().upper()
        if caracter == 'S':
            return 'S'
        elif caracter == 'N':
            return 'N'
        else:
            print('\nCaractere inválido. Digite novamente.')

def ao_cubo(n):
    return n ** 3

class TestCuboEEntrada(unittest.TestCase):
    def test_ao_cubo_positivo(self):
        self.assertEqual(ao_cubo(3), 27)

    def test_ao_cubo_zero(self):
        self.assertEqual(ao_cubo(0), 0)

    def test_ao_cubo_negativo(self):
        self.assertEqual(ao_cubo(-2), -8)

    def test_ler_carac_s(self):
        self.assertEqual(ler_carac(lambda _: 'S'), 'S')

    def test_ler_carac_n(self):
        self.assertEqual(ler_carac(lambda _: 'N'), 'N')

    def test_ler_carac_invalido_then_s(self):
        inputs = iter(['x', 'S']) 
        self.assertEqual(ler_carac(lambda _: next(inputs)), 'S')

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            numero = float(input('Digite um número: '))
            print(f'{numero} ao cubo é {ao_cubo(numero)}')
            if ler_carac() == 'N':
                break
        except ValueError:
            print('\nAlgo de errado não está certo, tente novamente.')'''