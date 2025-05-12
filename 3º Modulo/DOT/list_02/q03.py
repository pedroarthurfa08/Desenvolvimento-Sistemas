# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à daleitura.

import unittest
import random

def ler_numeros(n):
    return [float(input(f"Digite o número {i+1}: ")) for i in range(n)]

def imprimir_invertido(numeros):
    print("\nNúmeros em ordem inversa:")
    for num in reversed(numeros):
        print(num)

def main():
    n = int(input("Qual a quantidade de números? "))
    numeros = ler_numeros(n)
    imprimir_invertido(numeros)

class TestImprimirInvertido(unittest.TestCase):
    def test_imprimir_invertido(self):
        numeros = [1, 2, 3, 4, 5]
        import io
        import sys
        capturedOutput = io.StringIO() 
        sys.stdout = capturedOutput 
        imprimir_invertido(numeros)
        sys.stdout = sys.__stdout__ 
        self.assertIn("5", capturedOutput.getvalue())
        self.assertIn("4", capturedOutput.getvalue())
        self.assertIn("3", capturedOutput.getvalue())
        self.assertIn("2", capturedOutput.getvalue())
        self.assertIn("1", capturedOutput.getvalue())

if __name__ == "__main__":
    unittest.main(exit=False)
    main()