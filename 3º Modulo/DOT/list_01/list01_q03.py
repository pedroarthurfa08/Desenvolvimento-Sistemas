# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius. Fórmula: C = ((F-32)/9)*5

import unittest

def celsius(f):
    return (f - 32) * 5 / 9

class TestConversorTemperatura(unittest.TestCase):
    def test_zero_celsius(self):
        self.assertAlmostEqual(celsius(32), 0)

    def test_cem_celsius(self):
        self.assertAlmostEqual(celsius(212), 100)

    def test_temperatura_normal(self):
        self.assertAlmostEqual(celsius(98.6), 37, places=1)

    def test_temperatura_negativa(self):
        self.assertAlmostEqual(celsius(-22), -30)

if __name__ == '__main__':
    unittest.main(exit=False)

"""import unittest

def celsius(f):
    return (f - 32) * 5 / 9

class TestConversorTemperatura(unittest.TestCase):
    def test_zero_celsius(self):
        self.assertAlmostEqual(celsius(32), 0)

    def test_cem_celsius(self):
        self.assertAlmostEqual(celsius(212), 100)

    def test_temperatura_normal(self):
        self.assertAlmostEqual(celsius(98.6), 37, places=1)

    def test_temperatura_negativa(self):
        self.assertAlmostEqual(celsius(-22), -30)

if __name__ == '__main__':
    unittest.main(exit=False)

    while True:
        try:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            c = celsius(fahrenheit)
            print(f"\nA temperatura em Celsius é: {c:.2f}°C")
            break
        except ValueError:
            print("\nEntrada inválida. Digite um número.")"""