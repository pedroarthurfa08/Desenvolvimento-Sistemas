#questao01
'''
Programa que ler um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou ovalor booleano False (falso) caso contrário.'''
def vogal(caractere):
    vogal = "aeiouAEIOU"
    return caractere in vogal
def main():
    caractere = input("Será identificado se o caractere inserido é vogal ou não, portanto insira um caractere: ")
    resultado = (vogal(caractere))
    print(f"O caractere inserido é {resultado}")
if __name__=='__main__':
    main()