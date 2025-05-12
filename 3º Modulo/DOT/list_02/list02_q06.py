# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos e quantos faturamentos estão abaixo da média.

import unittest

def coletar_quantidade_precos(qnt):
    quantidade = []
    precos = []
    for i in range(qnt):
        qtd = int(input(f"Quantidade do produto {i + 1}: "))
        quantidade.append(qtd)
        prc = float(input(f"Valor do produto {i + 1}: $"))
        precos.append(prc)
    return quantidade, precos

def calcular_faturamento(quantidade, precos):
    faturamento = [q * p for q, p in zip(quantidade, precos)]
    return faturamento

def calcular_estatisticas(faturamento):
    faturamento_total = sum(faturamento)
    media_faturamento = faturamento_total / len(faturamento)
    abaixo_media = sum(1 for f in faturamento if f < media_faturamento)
    return faturamento_total, media_faturamento, abaixo_media

def main():
    qnt = 20
    print('Digite a quantidade e o preço de 20 produtos.')
    quantidade, precos = coletar_quantidade_precos(qnt)
    faturamento = calcular_faturamento(quantidade, precos)
    faturamento_total, media_faturamento, abaixo_media = calcular_estatisticas(faturamento)

    print("\nFaturamento individual de cada produto:")
    for i in range(qnt):
        print(f"Produto {i+1}: R$ {faturamento[i]:.2f}")
    print(f"\nFaturamento total: R$ {faturamento_total:.2f}")
    print(f"Média dos faturamentos: R$ {media_faturamento:.2f}")
    print(f"Quantidade de faturamentos abaixo da média: {abaixo_media}")

class TestCalcularFaturamento(unittest.TestCase):
    def test_calcular_faturamento(self):
        quantidade = [2, 3, 4]
        precos = [10.0, 20.0, 30.0]
        faturamento = calcular_faturamento(quantidade, precos)
        self.assertEqual(faturamento, [20.0, 60.0, 120.0])

if __name__ == "__main__":
    unittest.main(exit=False)
    
'''import unittest

def coletar_quantidade_precos(qnt):
    quantidade = []
    precos = []
    for i in range(qnt):
        qtd = int(input(f"Quantidade do produto {i + 1}: "))
        quantidade.append(qtd)
        prc = float(input(f"Valor do produto {i + 1}: $"))
        precos.append(prc)
    return quantidade, precos

def calcular_faturamento(quantidade, precos):
    faturamento = [q * p for q, p in zip(quantidade, precos)]
    return faturamento

def calcular_estatisticas(faturamento):
    faturamento_total = sum(faturamento)
    media_faturamento = faturamento_total / len(faturamento)
    abaixo_media = sum(1 for f in faturamento if f < media_faturamento)
    return faturamento_total, media_faturamento, abaixo_media

def main():
    qnt = 20
    print('Digite a quantidade e o preço de 20 produtos.')
    quantidade, precos = coletar_quantidade_precos(qnt)
    faturamento = calcular_faturamento(quantidade, precos)
    faturamento_total, media_faturamento, abaixo_media = calcular_estatisticas(faturamento)

    print("\nFaturamento individual de cada produto:")
    for i in range(qnt):
        print(f"Produto {i+1}: R$ {faturamento[i]:.2f}")
    print(f"\nFaturamento total: R$ {faturamento_total:.2f}")
    print(f"Média dos faturamentos: R$ {media_faturamento:.2f}")
    print(f"Quantidade de faturamentos abaixo da média: {abaixo_media}")

class TestCalcularFaturamento(unittest.TestCase):
    def test_calcular_faturamento(self):
        quantidade = [2, 3, 4]
        precos = [10.0, 20.0, 30.0]
        faturamento = calcular_faturamento(quantidade, precos)
        self.assertEqual(faturamento, [20.0, 60.0, 120.0])

if __name__ == "__main__":
    unittest.main(exit=False)
    main()'''