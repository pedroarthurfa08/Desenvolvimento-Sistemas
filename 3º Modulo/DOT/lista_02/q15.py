# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assimpor diante. Escrever todo a lista D e todo a lista E.

def invert_list(list):
    return list[::-1]

D = [int(input(f'Elemento {i + 1}: ')) for i in range(10)]

E = invert_list (D)

print('Lista D', D)
print('Lista E (inversa)', E)