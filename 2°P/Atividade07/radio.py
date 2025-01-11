class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.__volume_min = 0
        self.__volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estacoes = estacoes
        self.__volume = None
        self.__ligado = False
        self.__estacao_atual = None
        self.__frequencia_atual = None
        self.__antena_habilitada = False

    def ligar(self):
        self.__ligado = True
        self.__antena_habilitada = True
        self.__volume = self.__volume_min
        if self.__antena_habilitada:
            self.__frequencia_atual = list(self.__estacoes.keys())[0]
            self.__estacao_atual = self.__estacoes[self.__frequencia_atual]

    def desligar(self):
        self.__ligado = False
        self.__volume = None
        self.__frequencia_atual = None
        self.__estacao_atual = None

    def aumentar_volume(self, incremento=1):
        if not self.__ligado:
            return "O rádio está desligado."
        novo_volume = self.__volume + incremento
        if novo_volume > self.__volume_max:
            self.__volume = self.__volume_max
        else:
            self.__volume = novo_volume

    def diminuir_volume(self, decremento=1):
        if not self.__ligado:
            return "O rádio está desligado."
        novo_volume = self.__volume - decremento
        if novo_volume < self.__volume_min:
            self.__volume = self.__volume_min
        else:
            self.__volume = novo_volume

    def mudar_frequencia(self, frequencia=None):
        if not self.__ligado:
            return "O rádio está desligado."
        if frequencia:
            self.__frequencia_atual = frequencia
            self.__estacao_atual = self.__estacoes.get(frequencia, "Estação inexistente")
        else:
            frequencias = list(self.__estacoes.keys())
            indice_atual = frequencias.index(self.__frequencia_atual)
            proximo_indice = (indice_atual + 1) % len(frequencias)
            self.__frequencia_atual = frequencias[proximo_indice]
            self.__estacao_atual = self.__estacoes[self.__frequencia_atual]

    def status(self):
        return {
            "ligado": self.__ligado,
            "volume": self.__volume,
            "frequencia_atual": self.__frequencia_atual,
            "estacao_atual": self.__estacao_atual,
            "antena_habilitada": self.__antena_habilitada,
        }

estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

radio1 = RadioFM(vol_max=10, estacoes=estacoes)
radio2 = RadioFM(vol_max=15, estacoes=estacoes)
radio3 = RadioFM(vol_max=5, estacoes=estacoes)

radio1.ligar()
print(radio1.status())

radio1.aumentar_volume(3)
print(radio1.status())

radio1.mudar_frequencia()
print(radio1.status())

radio1.desligar()
print(radio1.status())
