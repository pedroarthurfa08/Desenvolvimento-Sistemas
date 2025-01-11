import random
import string
from datetime import datetime, timedelta

class CartaoEstacionamento:
    def __init__(self):
        self.numero = self._gerar_numero_cartao()
        self.data_hora_entrada = datetime.now()
        self.status = "ativo"
        self.data_hora_saida = None
        self.valor_total = 0.0

    def _gerar_numero_cartao(self):
        return ''.join(random.choices(string.digits, k=5))

    def registrar_saida(self):
        if self.status == "finalizado":
            raise ValueError("O cartão já está finalizado.")
        
        self.data_hora_saida = datetime.now()
        if self.data_hora_saida < self.data_hora_entrada:
            raise ValueError("A data e hora de saída não podem ser anteriores à data e hora de entrada.")
        
        self.valor_total = self._calcular_valor()
        self.status = "finalizado"

    def _calcular_valor(self):
        tempo_permanencia = self.data_hora_saida - self.data_hora_entrada
        minutos = tempo_permanencia.total_seconds() / 60
        horas = minutos // 60
        minutos_restantes = minutos % 60
        
        if horas < 2:
            return 8.0
        else:
            frações_adicionais = max(0, ((horas - 2) * 60 + minutos_restantes) // 15)
            return 8.0 + frações_adicionais * 0.50

    def consultar_valor_acumulado(self):
        if self.status == "finalizado":
            return self.valor_total
        else:
            agora = datetime.now()
            tempo_permanencia = agora - self.data_hora_entrada
            minutos = tempo_permanencia.total_seconds() / 60
            horas = minutos // 60
            minutos_restantes = minutos % 60

            if horas < 2:
                return 8.0
            else:
                frações_adicionais = max(0, ((horas - 2) * 60 + minutos_restantes) // 15)
                return 8.0 + frações_adicionais * 0.50

cartao1 = CartaoEstacionamento()
cartao2 = CartaoEstacionamento()
cartao3 = CartaoEstacionamento()

print("Cartão 1 - Entrada:", cartao1.data_hora_entrada)
print("Valor acumulado no momento:", cartao1.consultar_valor_acumulado())

cartao1.data_hora_saida = cartao1.data_hora_entrada + timedelta(hours=3, minutes=30)
cartao1.registrar_saida()

print("Cartão 1 - Saída:", cartao1.data_hora_saida)
print("Cartão 1 - Valor total:", cartao1.valor_total)
print("Cartão 1 - Status:", cartao1.status)