#questao02
'''
Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e 100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20. Por exemplo: Em 16.759 a soma dos dígitos é 1 + 6 + 7 + 5 + 9 = 31 é o valor retornado; Em 136.759 o valor lido é maior que 100 mil e deve retornar -1; Em -100 o valor lido é negativo e deve retornar -1.
'''
def calcular_soma_digitos(n):
    if 0 <= n < 100000:
        soma = sum(int(digito) for digito in str(n))
        return soma
    else:
        return -1
def main():
    n = int(input("Digite um número inteiro positivo menor que 100000: "))
    resultado = calcular_soma_digitos(n)
    print(resultado)

if __name__ == '__main__':
    main()