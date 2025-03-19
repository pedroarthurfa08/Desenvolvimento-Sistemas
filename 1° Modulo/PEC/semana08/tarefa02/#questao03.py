#questao03
'''
Escreva um programa que leia um número inteiro positivo e escreva na tela:
• FIZZ se o número é divisível por três;
• BUZZ se o número é divisível por cinco;
• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
• O próprio número caso não seja divisível por três ou por cinco.
OBS: para cada número lido apenas uma resposta deve ser impressa.
'''
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    elif n % 3 == 0:
        return "FIZZ"
    elif n % 5 == 0:
        return "BUZZ"
    else:
        return n
def main():
    try:
        n = int(input("Digite um número: "))
        if n <= 0:
            print()
            return
        result = fizzbuzz(n)
        print(result)
    except ValueError:
        print()
if __name__ == "__main__":
    main()