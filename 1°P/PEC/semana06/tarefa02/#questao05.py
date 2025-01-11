#questao05
'''
Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas!
Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:
°F = (°C * (9/5)) + 32'''
def temp(celsius):
    return (celsius * (9 / 5)) + 32
def main():
    celsius = float(input("Insira a temperatura em Celsius, para tranformamos em Fahrenheit:").strip())
    fahrenheit = (celsius * (9 / 5)) + 32
    temperatura = ("{:.2f}".format(fahrenheit))
    print(f'A temperatura de {celsius}° Celsius transformada em fahrenheit será de: {temperatura}° Fahrenheit.')
if __name__ =="__main__":
    main()