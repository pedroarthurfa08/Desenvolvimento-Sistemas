class Elevador:
    def __init__(self, total_andares, capacidade):
        self.__andar_atual = 0
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__ocupacao_atual = 0

    def subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
            print(f"Subindo... Andar atual: {self.__andar_atual}")
        else:
            print("Você já está no último andar.")

    def descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
            print(f"Descendo... Andar atual: {self.__andar_atual}")
        else:
            print("Você já está no térreo.")

    def entrar(self, pessoas=1):
        if self.__ocupacao_atual + pessoas <= self.__capacidade:
            self.__ocupacao_atual += pessoas
            print(f"Entraram {pessoas} pessoa(s). Ocupação atual: {self.__ocupacao_atual}")
        else:
            print("Capacidade do elevador atingida!")

    def sair(self, pessoas=1):
        if self.__ocupacao_atual - pessoas >= 0:
            self.__ocupacao_atual -= pessoas
            print(f"Saíram {pessoas} pessoa(s). Ocupação atual: {self.__ocupacao_atual}")
        else:
            print("Não há pessoas suficientes no elevador para sair.")


# Testando a classe
if __name__ == "__main__":
    print("--- Teste Elevador 1 ---")
    elevador1 = Elevador(total_andares=10, capacidade=5)
    elevador1.entrar(3)
    elevador1.subir()
    elevador1.subir()
    elevador1.sair(1)
    elevador1.descer()

    print("\n--- Teste Elevador 2 ---")
    elevador2 = Elevador(total_andares=5, capacidade=3)
    elevador2.entrar(2)
    elevador2.subir()
    elevador2.subir()
    elevador2.subir()
    elevador2.subir()
    elevador2.subir()  # Tentando ultrapassar

    print("\n--- Teste Elevador 3 ---")
    elevador3 = Elevador(total_andares=8, capacidade=4)
    elevador3.entrar(5)  # Ultrapassando capacidade
    elevador3.entrar(2)
    elevador3.sair(1)
    elevador3.subir()
    elevador3.descer()
    elevador3.descer()  # Tentando ir abaixo do térreo
