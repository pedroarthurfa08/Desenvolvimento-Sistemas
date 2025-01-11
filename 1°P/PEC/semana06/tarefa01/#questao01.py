#questao01 
'''
Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.'''
def ler(palavra):
    return len (palavra)
def main():
    palavra = input("Insira um nome e será informado quantos caracteres o nome possui: ")
    resultado = (ler(palavra))
    print(f'Aquantidade de caracteres na palavra {palavra} será de {resultado}.')
if __name__=='__main__':
    main()