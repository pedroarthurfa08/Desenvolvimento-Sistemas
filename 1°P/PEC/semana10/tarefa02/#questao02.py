#questao02
'''
Modifique a canção dos programadores do exercício anterior para incluir o refrão: Tecle “Ctrl+F5”.
Termine a canção com “Vamos fazer mais um café!”.
99 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
100 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
101 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
...
250 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
Vamos fazer mais um café!
'''
def main():
    for i in range(99, 251):
        print(f'{i} bugs no software, pegue um deles e conserte...\nTecle "Ctrl+F5"')
    print("Vamos fazer mais um café!")
if __name__ == "__main__":
    main()
