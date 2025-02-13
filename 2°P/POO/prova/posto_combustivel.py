class Combustivel:
    def __init__(self, preco_por_litro):
        self.preco_por_litro = preco_por_litro

    def calcular_valor(self, qtd_litros):
        raise NotImplementedError('Método calcular_valor() não implementado na classe base.')

class Gasolina(Combustivel):
    def __init__(self, preco_por_litro, aditivada):
        super().__init__(preco_por_litro)
        self.aditivada = aditivada

    def calcular_valor(self, qtd_litros):
        valor_base = qtd_litros * self.preco_por_litro
        if self.aditivada:
            return valor_base * 1.05
        return valor_base

class Etanol(Combustivel):
    def __init__(self, preco_por_litro, origem):
        super().__init__(preco_por_litro)
        self.origem = origem

class BombaDeCombustivel:
    def __init__(self, identificador):
        self.identificador = identificador
        self.combustivel = None

    def associar_combustivel(self, combustivel):
        self.combustivel = combustivel

    def abastecer(self, qtd_litros):
        if self.combustivel is None:
            raise ValueError("Bomba sem combustível associado.")
        total_pagar = self.combustivel.calcular_valor(qtd_litros)
        return Abastecimento(self, qtd_litros, total_pagar)

class Abastecimento:
    def __init__(self, bomba, qtd_litros, valor_total):
        self.bomba = bomba
        self.qtd_litros = qtd_litros
        self.valor_total = valor_total

    def __str__(self):
        tipo_combustivel = type(self.bomba.combustivel).__name__
        detalhes = "Aditivada" if isinstance(self.bomba.combustivel, Gasolina) and self.bomba.combustivel.aditivada else self.bomba.combustivel.origem
        return f"Bomba {self.bomba.identificador} ({tipo_combustivel} - {detalhes}): {self.qtd_litros} litros -> R$ {self.valor_total:.2f}"

class PostoDeCombustivel:
    def __init__(self, nome):
        self.nome = nome
        self.bombas = []

    def adicionar_bomba(self, bomba):
        self.bombas.append(bomba)

    def listar_bombas(self):
        return [f"Bomba {b.identificador}" for b in self.bombas]
