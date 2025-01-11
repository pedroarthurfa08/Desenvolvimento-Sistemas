#questao05
'''
Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo, se o número lido
for 5678 deverá ser mostrado 8765.
'''
print("Fazenedo um número ficar invertido!")
def invert(numero):
    u = numero % 10
    numero = numero // 10
    d = numero % 10
    numero = numero // 10
    c = numero % 10
    numero = numero // 10
    m = numero % 10
    numero_invertido = (u * 1000) + (d * 100) + (c * 10) + m
    return numero_invertido
def main():
    n=int(input("Insira um número, para que tal fique invertido:"))
    print(f'O número {n} invertido será {invert(n)}')
if __name__ =='__main__':
    main()