# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]
import unittest
import random

def gerar_numeros(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]

def eliminar_repeticoes(numeros):
    return list(dict.fromkeys(numeros))

class TestEliminarRepeticoes(unittest.TestCase):
    def test_eliminar_repeticoes(self):
        numeros = [1, 2, 2, 3, 4, 4, 5]
        resultado = eliminar_repeticoes(numeros)
        self.assertEqual(len(resultado), len(set(numeros)))
        self.assertTrue(all(n in resultado for n in set(numeros)))

    def test_eliminar_repeticoes_sem_repeticoes(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = eliminar_repeticoes(numeros)
        self.assertEqual(resultado, numeros)

    def test_eliminar_repeticoes_todos_repetidos(self):
        numeros = [1, 1, 1, 1, 1]
        resultado = eliminar_repeticoes(numeros)
        self.assertEqual(resultado, [1])

    def test_eliminar_repeticoes_lista_vazia(self):
        numeros = []
        resultado = eliminar_repeticoes(numeros)
        self.assertEqual(resultado, [])

if __name__ == "__main__":
    unittest.main(exit=False)