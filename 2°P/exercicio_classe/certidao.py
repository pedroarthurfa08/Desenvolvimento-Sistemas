from datetime import datetime

class Certidão:

    def __init__(self, nome, data, hora, cidade, estado, mae):
        self.nome = nome

        if not self.balidar_data(data):
            raise ValueError("Data Inválida")
        self.data = data
        if not self.validar_data(hora):
            raise ValueError("Hora inválida")
        
        self.data = data
        self.hora = hora
        self.cidade = cidade
        self.estado = estado
        self.mae = mae

def validar_data(self, data_str):
    try:
        data = datetime.strptime(data,"%D/%M/%Y")
        return data
    except ValueError:
        return False
    
def validar_hora(self, hora_str):
    try:
        hora = datetime.strptime(hora,"%H:%M")
        return hora
    except ValueError:
        return False
