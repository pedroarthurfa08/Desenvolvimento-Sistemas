# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

lista = []

for i in range(15):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    lista.append(valor)

maior = max(lista)
menor = min(lista)

posicao_maior = lista.index(maior)
posicao_menor = lista.index(menor)

print(f"\nO maior elemento é {maior} e está na posição {posicao_maior}.")
print(f"\nO menor elemento é {menor} e está na posição {posicao_menor}.")