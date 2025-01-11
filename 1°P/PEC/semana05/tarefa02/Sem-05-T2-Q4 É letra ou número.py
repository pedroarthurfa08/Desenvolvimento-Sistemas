#questao04
'''
 Programa que ler um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogalou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.
'''
def ver_caractere(caractere):
    return (caractere >= "a" and caractere <= "z") or (caractere >= "A" and caractere <= "Z") or (caractere >= "0" and caractere <= "9")
def main():
    caractere = input("Será identificado se o caractere inserido é letra ou não, portanto insira um caractere: ")
    resultado = (ver_caractere(caractere))
    print(f"O caractere inserido é {resultado}")
if __name__ =='__main__':
    main()