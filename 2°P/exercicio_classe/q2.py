class Bicicleta:
    def __init__(self, veloc_atual=0, altura_cela=0, calibragem_pneus=0):
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus
        self.veloc_max = 60  # km/h
        self.altura_cela_min = 0
        self.altura_cela_max = 10  # cm
        self.calibragem_pneus_min = 1
        self.calibragem_pneus_max = 5  # bar

    def acelerar(self):
        if self.veloc_atual < self.veloc_max:
            self.veloc_atual += 1
        else:
            print("Velocidade máxima alcançada.")

    def frear(self):
        if self.veloc_atual > 0:
            self.veloc_atual -= 1
        else:
            print("Bicicleta parada.")

    def regular_cela(self, altura):
        if self.veloc_atual == 0:
            if self.altura_cela_min <= altura <= self.altura_cela_max:
                self.altura_cela = altura
            else:
                print("Altura inválida. Altura mínima: {} cm, Altura máxima: {} cm".format(self.altura_cela_min, self.altura_cela_max))
        else:
            print("Não é possível regular a cela enquanto a bicicleta está em movimento.")

    def calibrar_pneus(self, pressao):
        if self.veloc_atual == 0:
            if self.calibragem_pneus_min <= pressao <= self.calibragem_pneus_max:
                self.calibragem_pneus = pressao
            else:
                print("Pressão inválida. Pressão mínima: {} bar, Pressão máxima: {} bar".format(self.calibragem_pneus_min, self.calibragem_pneus_max))
        else:
            print("Não é possível calibrar os pneus enquanto a bicicleta está em movimento.")

    def imprimir_status(self):
        print("Velocidade atual: {} km/h".format(self.veloc_atual))
        print("Altura da cela: {} cm".format(self.altura_cela))
        print("Calibragem dos pneus: {} bar".format(self.calibragem_pneus))
