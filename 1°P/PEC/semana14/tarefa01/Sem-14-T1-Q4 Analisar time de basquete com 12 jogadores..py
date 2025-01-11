'''Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura dos jogadores, determine: a. o nome e a altura do jogador mais alto; b. a média de altura do time; c. os jogadores com altura superior à média, listando o nome e a altura de cada um.'''
def jogador_mais_alto(jogadores):
    mais_alto = jogadores[0]
    for jogador in jogadores:
        if jogador[1] > mais_alto[1]:
            mais_alto = jogador
    return mais_alto

def media_altura(jogadores):
    soma_alturas = 0
    for jogador in jogadores:
        soma_alturas += jogador[1]
    return soma_alturas / len(jogadores)

def jogadores_acima_media(jogadores, media):
    acima_media = []
    for jogador in jogadores:
        if jogador[1] > media:
            acima_media.append(jogador)
    return acima_media

def main():
    jogadores = []
    for i in range(12):
        nome = input()
        altura = float(input())
        jogadores.append((nome, altura))

    mais_alto = jogador_mais_alto(jogadores)
    print("JOGADOR MAIS ALTO DO TIME")
    print(f"{mais_alto[0]}\n{mais_alto[1]:.2f}")

    media = media_altura(jogadores)
    print("ALTURA MÉDIA DO TIME")
    print(f"{media:.2f}")

    acima_media = jogadores_acima_media(jogadores, media)
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for jogador in acima_media:
        print(f"{jogador[0]}\n{jogador[1]:.2f}")

if __name__ == "__main__":
    main()
