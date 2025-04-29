# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos e quantos faturamentos estão abaixo da média.

quantidade = []
precos = []
faturamento = []

print('Digite a quantidade de 20 produtos.')

for i in range(20):
    qtd = int(input(f"Quantidade do produto {i + 1}: "))
    quantidade.append(qtd)

for i in range(20):
    prc = float(input(f"Valor do produto {i + 1}: $"))
    precos.append(prc)

for i in range(20):
    fat = quantidade * precos
    faturamento.append(fat)

faturamento_total = sum(faturamento)

media_faturamento = faturamento_total / 20

abaixo_media = sum (1 for f in faturamento if f < faturamento_total)

print("\nFaturamento individual de cada produto:")
for i in range(20):
    print(f"Produto {i+1}: R$ {faturamento[i]:.2f}") 

print(f"\nFaturamento total: R$ {faturamento_total:.2f}")
print(f"Média dos faturamentos: R$ {media_faturamento:.2f}")
print(f"Quantidade de faturamentos abaixo da média: {abaixo_media}")