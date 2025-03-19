print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')
total = 0 

turno_jogador = 1

while total < 21:
    print(f'Total atual: {total}')
    escolha = int(input(f' Jogador {turno_jogador}, escolha um número de 1 a 10:'))
    if escolha < 1 or escolha > 10:
       print("Escolha inválida! Escolha um número entre 1 e 10")
    total += escolha
    if total >= 21:
      print(f"Jogador {turno_jogador} perdeu!")
      break
    turno_jogador = 2 if turno_jogador == 1 else 1
print("Fim do jogo!")