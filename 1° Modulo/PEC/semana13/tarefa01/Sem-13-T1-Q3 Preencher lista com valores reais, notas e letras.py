'''Escreva um programa que leia um número n. Considere uma lista com n posições, e então: a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais. b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.'''
def ler_valores(n):
    valores = []
    for _ in range(n):
        valor = float(input())
        valores.append(valor)
    return valores

def ler_notas(n):
    notas = []
    for _ in range(n):
        nota = float(input())
        notas.append(nota)
    return notas

def ler_letras(n):
    letras = []
    for _ in range(n):
        letra = input()[0]
        letras.append(letra)
    return letras

def contar_vogais_e_consoantes(letras):
    vogais = "aeiouAEIOU"
    num_vogais = 0
    consoantes = []
    for letra in letras:
        if letra in vogais:
            num_vogais += 1
        elif (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
            consoantes.append(letra)
    return num_vogais, consoantes

def main():
    n = int(input())
    if n > 0:
        valores = ler_valores(n)
        valores_inversos = [float(f"{valores.pop():.4f}") for _ in range(n)]
        print(valores_inversos)
    else:
        print([])

    if n > 0:
        notas = ler_notas(n)
        notas_formatadas = [float(f"{nota:.1f}") for nota in notas]
        media = sum(notas) / len(notas)
        print(notas_formatadas)
        print(float(f"{media:.1f}"))
    else:
        print([])
        print("SEM NOTAS")

    if n > 0:
        letras = ler_letras(n)
        num_vogais, consoantes = contar_vogais_e_consoantes(letras)
        print(num_vogais)
        print(consoantes)
    else:
        print(0)
        print([])

if __name__ == "__main__":
    main()