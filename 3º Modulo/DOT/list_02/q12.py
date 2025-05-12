# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# =====MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0)Sair do programa
# ——————–
# Digite sua escolha:_
# 12) Deseja-se publicar

import unittest

def calcular_acertos(gabarito, respostas):
    return sum(1 for g, r in zip(gabarito, respostas) if g == r)

def ler_gabarito():
    gabarito = []
    for i in range(30):
        while True:
            resposta = input(f"Digite a resposta da questão {i+1} do gabarito (A, B, C, D ou E): ").strip().upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                gabarito.append(resposta)
                break
            else:
                print("Resposta inválida. Por favor, digite A, B, C, D ou E.")
    return gabarito

def ler_respostas_aluno(numero_aluno):
    respostas = []
    for i in range(30):
        while True:
            resposta = input(f"Digite a resposta da questão {i+1} do aluno {numero_aluno} (A, B, C, D ou E): ").strip().upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                respostas.append(resposta)
                break
            else:
                print("Resposta inválida. Por favor, digite A, B, C, D ou E.")
    return respostas

class TestCalcularAcertos(unittest.TestCase):
    def test_calcular_acertos(self):
        gabarito = ['A'] * 30
        respostas = ['A'] * 30
        self.assertEqual(calcular_acertos(gabarito, respostas), 30)

    def test_calcular_acertos_parcial(self):
        gabarito = ['A'] * 30
        respostas = ['A'] * 15 + ['B'] * 15
        self.assertEqual(calcular_acertos(gabarito, respostas), 15)

def main():
    gabarito = ler_gabarito()
    
    while True:
        try:
            num_alunos = int(input("Digite o número de alunos: "))
            if num_alunos > 0:
                break
            else:
                print("O número de alunos deve ser maior que 0.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")
            
    for i in range(num_alunos):
        respostas_aluno = ler_respostas_aluno(i+1)
        acertos = calcular_acertos(gabarito, respostas_aluno)
        print(f"O aluno {i+1} acertou {acertos} questões.")

if __name__ == "__main__":
    unittest.main(exit=False)
    main()