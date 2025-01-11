'''Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de duas temperaturas, com (temperatura, escala), e mostre qual é a maior. Use upper() e colchetes [] para garantir a leitura correta, por exemplo: escala = input('Escala : ').upper()[0]'''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def maior_temperatura(temp1, temp2):
    valor1, escala1 = temp1
    valor2, escala2 = temp2
    
    if escala1 == escala2:
        if valor1 > valor2:
            return temp1
        else:
            return temp2
    else:
        if escala1 == 'C':
            valor1_convertido = celsius_to_fahrenheit(valor1)
            if valor1_convertido > valor2:
                return temp1
            else:
                return temp2
        else:
            valor2_convertido = celsius_to_fahrenheit(valor2)
            if valor1 > valor2_convertido:
                return temp1
            else:
                return temp2

def main():
    temp1 = (float(input()), input().upper()[0])
    temp2 = (float(input()), input().upper()[0])

    maior = maior_temperatura(temp1, temp2)
    print(maior)

if __name__ == "__main__":
    main()
