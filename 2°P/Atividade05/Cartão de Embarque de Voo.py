from datetime import datetime

assentos_por_voo = {}

class CartaoEmbarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data_hora_embarque):
        self.nome_passageiro = nome_passageiro
        self.numero_voo = numero_voo

        if len(codigo_reserva) == 6 and codigo_reserva.isalnum():
            self.codigo_reserva = codigo_reserva
        else:
            raise ValueError("O código de reserva deve ter 6 caracteres alfanuméricos.")

        if data_hora_embarque > datetime.now():
            self.data_hora_embarque = data_hora_embarque
        else:
            raise ValueError("A data e hora do embarque não podem ser retroativas.")

        self.check_in_realizado = False
        self.assento = None

        if numero_voo not in assentos_por_voo:
            assentos_por_voo[numero_voo] = [f"{fila}{coluna}" for fila in "ABCDEF" for coluna in range(1, 31)]
        self.assentos_disponiveis = assentos_por_voo[numero_voo]

    def realizar_check_in(self):
        if self.check_in_realizado:
            raise ValueError("O check-in já foi realizado.")
        if not self.assentos_disponiveis:
            raise ValueError("Não há assentos disponíveis.")
        
        self.assento = self.assentos_disponiveis.pop(0)
        self.check_in_realizado = True

    def alterar_assento(self, novo_assento):
        if not self.check_in_realizado:
            raise ValueError("O check-in ainda não foi realizado.")
        if novo_assento not in self.assentos_disponiveis:
            raise ValueError("O assento solicitado não está disponível.")
        
        if self.assento:
            self.assentos_disponiveis.append(self.assento)
        
        self.assento = novo_assento
        self.assentos_disponiveis.remove(novo_assento)

    def __str__(self):
        return (f"Cartão de Embarque:\n"
                f"Passageiro: {self.nome_passageiro}\n"
                f"Voo: {self.numero_voo}\n"
                f"Localizador: {self.codigo_reserva}\n"
                f"Data/Hora do Embarque: {self.data_hora_embarque}\n"
                f"Check-in Realizado: {'Sim' if self.check_in_realizado else 'Não'}\n"
                f"Assento: {self.assento if self.assento else 'Não definido'}")