import time

class Microondas:
    def __init__(self, potencia_min, potencia_max, tempo_min, tempo_max, potencia=None, tempo=None, ligado=False):
        # Definição dos atributos e validação inicial
        self.potencia_min = potencia_min
        self.potencia_max = potencia_max
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max
        
        self.potencia = potencia if potencia_min <= potencia <= potencia_max else potencia_min
        self.tempo = tempo if tempo_min <= tempo <= tempo_max else tempo_min
        self.ligado = ligado

    # Método para ligar o micro-ondas
    def ligar(self):
        self.ligado = True
        print("Micro-ondas ligado.")

    # Método para desligar o micro-ondas
    def desligar(self):
        self.ligado = False
        print("Micro-ondas desligado.")

    # Método para configurar o tempo
    def configurar_tempo(self, tempo):
        if self.tempo_min <= tempo <= self.tempo_max:
            self.tempo = tempo
            print(f"Tempo configurado para {self.tempo} segundos.")
        else:
            print(f"Tempo inválido. Escolha entre {self.tempo_min} e {self.tempo_max} segundos.")

    # Método para configurar a potência
    def configurar_potencia(self, potencia):
        if self.potencia_min <= potencia <= self.potencia_max:
            self.potencia = potencia
            print(f"Potência configurada para {self.potencia}.")
        else:
            print(f"Potência inválida. Escolha entre {self.potencia_min} e {self.potencia_max}.")

    # Método para iniciar o funcionamento
    def iniciar(self):
        if self.ligado:
            print(f"Micro-ondas iniciando... Tempo: {self.tempo} segundos, Potência: {self.potencia}.")
            while self.tempo > 0:
                print(f"Tempo restante: {self.tempo} segundos...")
                time.sleep(1)  # Simula o tempo passando (1 segundo)
                self.tempo -= 1
            print("Aquecimento concluído!")
        else:
            print("O micro-ondas está desligado. Ligue-o antes de iniciar.")

    # Método para exibir o estado atual do micro-ondas
    def estado(self):
        ligado_str = "ligado" if self.ligado else "desligado"
        print(f"Micro-ondas {ligado_str} - Tempo: {self.tempo} segundos, Potência: {self.potencia}")

# Criação de objetos
micro1 = Microondas(potencia_min=1, potencia_max=10, tempo_min=10, tempo_max=300, potencia=5, tempo=60)
micro2 = Microondas(potencia_min=1, potencia_max=10, tempo_min=10, tempo_max=600, potencia=7, tempo=120)
micro3 = Microondas(potencia_min=1, potencia_max=5, tempo_min=5, tempo_max=120, potencia=3, tempo=30)

# Estados iniciais
print("Estados iniciais:")
micro1.estado()
micro2.estado()
micro3.estado()

# Testando métodos
print("\nTestando Micro-ondas 1:")
micro1.ligar()
micro1.configurar_tempo(90)
micro1.configurar_potencia(8)
micro1.iniciar()
micro1.desligar()
micro1.estado()

print("\nTestando Micro-ondas 2:")
micro2.ligar()
micro2.configurar_tempo(600)  # Tempo máximo
micro2.configurar_potencia(10)  # Potência máxima
micro2.iniciar()
micro2.desligar()
micro2.estado()

print("\nTestando Micro-ondas 3:")
micro3.ligar()
micro3.configurar_tempo(15)
micro3.configurar_potencia(2)
micro3.iniciar()
micro3.desligar()
micro3.estado()
