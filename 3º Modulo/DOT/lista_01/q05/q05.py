#5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
#1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
#- para homens : (72.7 * h) – 58
#- para mulheres : (62.1 * h) – 44.7
#Observação: Altura = h (na fórmula acima).

def altura(h, sexo):
    if sexo == 1:
        return (62.1 * h) - 44.7
    elif sexo == 2:
        return (72.7 * h) - 58
    else:
        return None

for _ in range(1):
    try:
        sexo = int(input("\nDigite seu 1 para mulher e 2 para homem: "))
        if sexo not in[1, 2]:
            print("\nOpção Inválida!")
            break

        h = float(input("\nInforme sua altura em metros: "))
        print("\nSeu peso ideal é: %.2f kg" %altura(h, sexo))

    except ValueError:
        print("\nAlgo de errado não está certo, tente novamente.")