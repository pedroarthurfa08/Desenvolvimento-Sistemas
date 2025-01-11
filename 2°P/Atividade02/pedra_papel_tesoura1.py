import random

def escolha_usuario():
    escolha = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ").strip().lower()
    if escolha in ("pedra", "papel", "tesoura"):
        return escolha
    elif escolha == "sair":
        return None
    else:
        print("Escolha inválida, tente novamnete.")
        return escolha_usuario()

def escolha_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def vencedor(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or \
        (usuario == "tesoura" and computador == "papel") or \
        (usuario == "papel" and computador == "pedra"):
        return "Você venceu!"
    else:
        return "Você perdeu e o pc ganhou!"
        
def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    while True:
        usuario = escolha_usuario()
        if usuario is None:
            print("Encerrando o jogo...")
            break
        computador = escolha_computador()
        print(f"Computador escolheu: {computador}")

        resultado = vencedor(usuario, computador)
        print(resultado)
main()