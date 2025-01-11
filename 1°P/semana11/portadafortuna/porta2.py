from random import*

jogando = True
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
while jogando == True:

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
        print("\nVocê que jogar de novo? (s/n)")
        resposta = input()
        if resposta == 'n' or 'N' or 'nao' or 'Não' or 'não' or 'Nao':
            jogando = False
print(" Obrigado por jogar.")
print(" Sua pontuação final é de", score)
