class Gato:
    rg = 0
    def __init__(self, nome, peso, idade):
        Gato.rg += 1
        self.rg = Gato.rg
        self.nome = nome
        self.peso = peso
        self.idade = idade

