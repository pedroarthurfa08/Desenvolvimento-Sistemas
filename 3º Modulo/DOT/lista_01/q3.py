'''3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius. Fórmula: C = ((F-32)/9)*5 ''' 

def celsius(f):
    return ((f-32)/9)*5

while True:
    try:
        f = float(input("Digite a temperatura em Celsius: "))
        print("\no perímetro do cículo é %2f" % celsius(f))
        break
    except:
        print("\nAlgo de errado não está certo, tente novamente.")