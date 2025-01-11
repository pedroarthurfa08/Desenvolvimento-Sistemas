from random import*
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
       


Escolha uma porta (1, 2, 3):
''')
for attempt in range(3):

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
    print(f'VocÊ acertou {score} entre as três portas.')