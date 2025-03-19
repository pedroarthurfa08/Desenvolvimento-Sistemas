def soma(a, b, imprime=False):
    if imprime:
        print('{}+{}={}'.format(a,b,(a+b)))
    return a+b
a = soma(7, 3)
print('a=',a)
soma(7,3, True)