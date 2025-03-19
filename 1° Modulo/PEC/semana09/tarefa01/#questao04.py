#questao04
'''
Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.
'''
def num(a, b):
    return a - b if a > b else b - a 
def main():
    n1 = int(input("Digite primeiro número: "))
    n2 = int(input("Digite segundo número: "))
    n3 = int(input("Digite terceiro número: "))
    dif1 = num(n1, n2)
    dif2 = num(n1, n3)
    print(f'O menor número da diferença entre o segundo e o primeiro e o terceiro como o primeiro é {dif1 if dif1 < dif2 else dif2}')
if __name__ == "__main__":
    main()