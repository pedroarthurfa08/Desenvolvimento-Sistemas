#1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.

def par_impar(x):
    if x % 2 == 0:
        return True
    else: 
        return False

while True:
    try:  
        num = int(input("\nDigite um número: "))
        if par_impar(num):
            print("\nO número %d é par." %num)
        else:
            print("\nO número %d é ímpar." %num)
        break
    except:
        print("\nAlgo de errado não está certo, tente novamente.")