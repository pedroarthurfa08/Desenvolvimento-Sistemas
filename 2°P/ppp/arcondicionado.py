class ArCondicionado:
    def __init__(self, temp_min=16, temp_max=30, vel_min=1, vel_max=5, temperatura=24, velocidade=3, modo='automático'):
        self.__temp_min = temp_min
        self.__temp_max = temp_max
        self.__vel_min = vel_min
        self.__vel_max = vel_max
        
        self.__temperatura = self.__validar_temperatura(temperatura)
        self.__velocidade = self.__validar_velocidade(velocidade)
        self.__modo = self.__validar_modo(modo)
        self.__ligado = False

    def __validar_temperatura(self, temperatura):
        if self.__temp_min <= temperatura <= self.__temp_max:
            return temperatura
        raise ValueError(f"Temperatura fora do limite permitido ({self.__temp_min}-{self.__temp_max}°C)")

    def __validar_velocidade(self, velocidade):
        if self.__vel_min <= velocidade <= self.__vel_max:
            return velocidade
        raise ValueError(f"Velocidade fora do limite permitido ({self.__vel_min}-{self.__vel_max})")

    def __validar_modo(self, modo):
        modos_validos = ['automático', 'frio', 'ventilar']
        if modo in modos_validos:
            return modo
        raise ValueError("Modo inválido! Escolha entre: 'automático', 'frio', 'ventilar'.")

    def ligar(self):
        self.__ligado = True
        print("Ar-condicionado ligado.")

    def desligar(self):
        self.__ligado = False
        print("Ar-condicionado desligado.")

    def aumentar_temperatura(self):
        if self.__ligado and self.__temperatura < self.__temp_max:
            self.__temperatura += 1
        else:
            print("Não é possível aumentar a temperatura.")

    def diminuir_temperatura(self):
        if self.__ligado and self.__temperatura > self.__temp_min:
            self.__temperatura -= 1
        else:
            print("Não é possível diminuir a temperatura.")

    def aumentar_velocidade(self):
        if self.__ligado and self.__modo != 'automático' and self.__velocidade < self.__vel_max:
            self.__velocidade += 1
        else:
            print("Não é possível aumentar a velocidade.")

    def diminuir_velocidade(self):
        if self.__ligado and self.__modo != 'automático' and self.__velocidade > self.__vel_min:
            self.__velocidade -= 1
        else:
            print("Não é possível diminuir a velocidade.")

    def mudar_modo(self, modo):
        if modo == 'automático':
            self.__velocidade = self.__vel_min
        self.__modo = self.__validar_modo(modo)
        print(f"Modo alterado para: {self.__modo}")

    def __str__(self):
        estado = "Ligado" if self.__ligado else "Desligado"
        return (f"Ar-Condicionado [{estado}]\n"
                f"Temperatura: {self.__temperatura}°C\n"
                f"Velocidade: {self.__velocidade}\n"
                f"Modo: {self.__modo}")

if __name__ == "__main__":
    ar1 = ArCondicionado(temperatura=22, velocidade=2, modo='frio')
    ar2 = ArCondicionado(temperatura=25, velocidade=4, modo='ventilar')
    ar3 = ArCondicionado(temperatura=18, velocidade=1, modo='automático')

    print("=== Estados Iniciais ===")
    print(ar1)
    print(ar2)
    print(ar3)

    ar1.ligar()
    ar1.aumentar_temperatura()
    ar1.aumentar_velocidade()
    ar1.mudar_modo('automático')

    ar2.ligar()
    ar2.diminuir_temperatura()
    ar2.diminuir_velocidade()

    ar3.ligar()
    ar3.aumentar_temperatura()
    ar3.mudar_modo('frio')
    ar3.aumentar_velocidade()

    print("\n=== Estados Finais ===")
    print(ar1)
    print(ar2)
    print(ar3)
