# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes ocorreu a letra ‘A’.
#OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

def validar_entrada(entrada):
    if entrada.isalpha():
        return True
    else:
        return False

entrada_usuario = input("Digite uma lista de letras (sem espaços ou números): ").strip()

while not validar_entrada(entrada_usuario):
    print("Entrada inválida. A lista deve conter apenas letras.")
    entrada_usuario = input("Digite uma lista de letras (sem espaços ou números): ").strip()

lista_letras = list(entrada_usuario.upper())  

contagem_a = lista_letras.count('A')

print(f"A letra 'A' aparece {contagem_a} vezes na lista.")
