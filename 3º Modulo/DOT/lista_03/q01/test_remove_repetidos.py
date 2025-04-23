# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

from remover_repetidos import remover_repetidos

def test_list_sem_repetidos():
    assert remove_repetidos([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]

def test_list_com_repetidos():
    assert remove_repetidos([1, 2, 3]) == [1, 2, 3]

def list_vazia():
    assert remove_repetidos ([]) == []

def list_todos_iguais():
    assert remover_repetidos([9, 9, 9]) ==[9]

def list_numeros_negativos():
    assert remover_repetidos([-1, -2, -1, -2 , 0]) == [-1, -2, 0]

