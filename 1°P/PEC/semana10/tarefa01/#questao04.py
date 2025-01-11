#questao04
'''
Escreva um programa que gere a seguinte sequência:

10, 20, 30, 40, ..., 990, 1000.

Considere a separação dos números por vírgula seguido de espaço em branco e o ponto no final da
sequência.
'''
def main():
    seguido = ""
    for i in range (10, 1001, 10):
        seguido += str(i) + ", "
    seguido = seguido[:-2] + "."
    print("Será escrito um sequência de números que ira de 10 a 1000, sempre de 10 em 10 números:")
    print (seguido)
if __name__ == "__main__":
    main()