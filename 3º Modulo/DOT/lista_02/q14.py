# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.

def modificar_lista(lista):
    for i in range(len(lista)):
        if lista [i] < 0:
            lista [i] = 0
    return lista

C = [int(input(f'Elemento {i + 1}: ')) for i in range(10)]

C_modificada = modificar_lista(C)

print("Lista C modificada", C_modificada)