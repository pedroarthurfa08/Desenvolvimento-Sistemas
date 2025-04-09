# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face. 

n = 10 
resultados = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

contagem_lados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for  resultado in resultados:
    if 1 <= resultado <= 6:
        contagem_lados[resultado] += 1

for face, contagem in contagem_lados.items():
    print(f'Face {face}: {contagem} ocorrência(s)')