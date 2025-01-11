#questao03
'''
Programa que ler um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE ou o valor booleano False (falso) caso contrário.'''
def consoante(letra):
    consoantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    return letra in consoantes
def main():
    letra = input("Será identificado se o caractere inserido é consoante ou não, portanto insira um caractere: ")
    resultado = (consoante(letra))
    print(f"O caractere inserido é {resultado}")
if __name__=='__main__':
    main()