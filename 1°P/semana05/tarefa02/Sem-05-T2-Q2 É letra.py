#questao02
'''
Programa que ler um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.'''
def letra(caractere):
    letras = ("qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM")
    return caractere in letras
caractere = input("Será identificado se o caractere inserido é letra ou não, portanto insira um caractere: ")
resultado = (letra(caractere))
print(f"O caractere inserido é {resultado}")