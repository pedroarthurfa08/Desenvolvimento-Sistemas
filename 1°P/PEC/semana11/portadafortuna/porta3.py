from random import*

tentativa = 0
score = 0
print('''
Porta da Fortuna!
=================
Existe um super prêmio atrás de um das destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
     __________            __________            __________
    |          |          |          |          |          |
    |    [1]   |          |    [2]   |          |    [3]   |
    |          |          |          |          |          |
    |          |          |          |          |          |
    |         °|          |         °|          |         °|
    |__________|          |__________|          |__________|  
''')
while score < 3:

    tentativa += 1

    print("\nTentativa", tentativa, ": Escolha uma porta(1, 2 ou 3):")

    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1, 3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score += 1
    else:
        print("Que peninha!")
        print(f'Você acertou {score} entre as três portas.')
    print("\n**Você conseguiu! Terminou o jogo em", tentativa, "tentaticas**")
        
