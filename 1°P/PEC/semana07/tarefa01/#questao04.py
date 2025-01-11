#questao04
'''
Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou
“símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.
'''
def ler(caracter):
    vogal = "AEIOU"
    consoante = "BCDFGHJKLMNPQRSTVWXYZ"
    numero = "0123456789"
    if caracter in vogal:
        return 'vogal'
    elif caracter in consoante:
        return 'consoante'
    elif caracter in numero:
        return 'número'
    else:
        return 'símbolo'    
def main():
    caracter = input("Insira um caractere: ").upper()
    resultado = (ler(caracter))
    print(f'O caractere "{caracter}" pode ser identificado como um(a) {resultado}.')
if __name__=="__main__":
    main()