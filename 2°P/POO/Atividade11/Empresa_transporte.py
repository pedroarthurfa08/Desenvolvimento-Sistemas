class Veiculo:
    def __init__(self, chassi, ano):
        self.__chassi = chassi
        self.__ano = ano
    
    def __str__(self):
        return f'Chassi: {self._chassi}\nAno: {self._ano}'

class moto(Veiculo):
    def __init__(self, chassi, ano, cilindadras):
         super().__init__(chassi, ano)
         self._cilindradas = cilindadras
         self._consumo = 25

    def calcula_custo(self, distancia, preço_comb):
        litros = distancia / self._consumo
        return litros*preço_comb

    def __str__(self):
        return super().__str__() + f'\nCilindradas: {self._cilindradas}\nConsumo:{self._consumo}'
    
class carro(Veiculo):
    def __init__(self, chassi, ano, motor):
         super().__init__(chassi, ano)
         self.motor = motor
         self._consumo = 12
    
    def calcula_custo(self, distancia, preço_comb):
        litros = distancia / self._consumo
        return litros*preço_comb
    
    def __str__(self):
        return super().__str__() + f'\motor: {self.motor}\nConsumo:{self._consumo}'
    
class caminhão(Veiculo):
    def __init__(self, chassi, ano, capacidade):
         super().__init__(chassi, ano)
         self.motor = capacidade
         self._consumo = 5
    
    def calcula_custo(self, distancia, preço_comb):
        litros = distancia / self._consumo
        return litros*preço_comb
    
    def __str__(self):
        return super().__str__() + f'\capacidade: {self.capacidade}\nConsumo:{self._consumo}'
    
class Controle_Viagens:
    def __init__(self):
        self._veiculos =[]
        self._total_custo = 0

    def adicionar_veiculos(self,veiculo):
        self._ceiculos.append(veiculo)

    def lista_veiculos(self):
        for veiculos in self._veiculos:
            print(veiculos)
    
    def calcula_custo_total(self, veiculos, distancia, preço_comb):
        self._total_custo += veiculos.calcula_custo(distancia, preço_comb)
        return self._total_custo