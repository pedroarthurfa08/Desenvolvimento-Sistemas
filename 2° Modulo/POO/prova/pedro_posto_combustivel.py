class PostoDeCombustivel:
    def __init__(self, nome):
        self._nome = nome
        self._bombas = []
        
    def adicionar_bomba(self, bomba):
        if isinstance(bomba, BombaDeCombustivel):
            self._bombas.append(bomba)
            return f'Cadastrando bomba {bomba._identificador} ao posto {self._nome}...'
        else:
            raise TypeError('Bomba inválida. A bomba deve ser do tipo BombaDeCombustivel.')

    def listar_bombas(self):
        lista_bombas_formatada = [f'Bomba: {bomba._identificador}' for bomba in self._bombas]
        return ', '.join(lista_bombas_formatada)
   
class BombaDeCombustivel:
    contadorId = 0
    def __init__(self):
        BombaDeCombustivel.contadorId += 1
        self._identificador = BombaDeCombustivel.contadorId
        self._combustivel = None
        
    def associar_combustivel(self, combustivel):
        if isinstance(combustivel, Combustivel):
            self._combustivel = combustivel
            return f'Associando {self._combustivel} à bomba {self._identificador}...'
        else:
            raise TypeError('Combustível inválido. O combustível deve ser do tipo Combustivel.')

    def abastecer(self, qtd_litros, controle):
        if isinstance(self._combustivel, Combustivel):
            if isinstance(qtd_litros, (float, int)):
                if qtd_litros > 0:
                    if isinstance(controle, Controle_De_Abastecimentos):
                        abastecimento = Abastecimento(self, qtd_litros)
                        controle.registrar_abastecimento(abastecimento)
                        return f'Realizando abastecimento na bomba {self._identificador}: {qtd_litros} litros...\nTotal a pagar: R$ {abastecimento._valor:.2f}'
                    else:
                        raise TypeError('Controle inválido. O controle deve ser da classe Controle_De_Abastecimento')
                else:
                    raise ValueError('Quantidade de litros deve ser maior que zero.')
            else:
                raise TypeError('Quantidade de litros deve ser um float ou inteiro.')
        else:
            raise TypeError('Combustível inválido. O combustível não foi associado a essa bomba.')
        
# Superclasse
class Combustivel:
    def __init__(self, nome, preco_por_litro):
        lista_nomes = ['Gasolina', 'Etanol']
        nome_capitalizado = nome.capitalize()
        if nome_capitalizado in lista_nomes:
            self._nome = nome_capitalizado
        else:
            raise ValueError('Nome inválido. O nome deve ser "Gasolina" ou "Etanol".')
        
        if isinstance(preco_por_litro, (float, int)):
            if preco_por_litro > 0:
                self._preco_por_litro = preco_por_litro
            else:
                raise ValueError('Preço por litro deve ser maior que zero.')
        else:
            raise TypeError('Preço por litro deve ser um float ou inteiro.')

    def calcular_valor(self, qtd_litros):
        raise NotImplementedError('Método não implementado na superclasse')
    
    def __str__(self):
        return f'{self._nome} genérico.'
    
# Subclasse
class Gasolina(Combustivel):
    def __init__(self, preco_por_litro, aditivada):
        super().__init__('Gasolina', preco_por_litro)
        if aditivada.lower() == 'sim':
            self._aditivada = True
        elif aditivada.lower() == 'não':
            self._aditivada = False
        else:
            raise ValueError('Aditivada deve ser "Sim" ou "Não".')

    def calcular_valor(self, qtd_litros):
        return qtd_litros * self._preco_por_litro

    def __str__(self):
        return f'Gasolina {'Aditivada' if self._aditivada else 'Não aditivada'}'
    
class Etanol(Combustivel):
    def __init__(self, preco_por_litro, origem):
        super().__init__('Etanol', preco_por_litro)
        self._lista_origem = ['Cana de açucar', 'Milho']
        origem_capitalizado = origem.capitalize()
        if origem_capitalizado in self._lista_origem:
            self._origem = origem_capitalizado
        else:
            raise ValueError('Origem inválida. A origem deve ser "Cana de açucar" ou "Milho".')

    def calcular_valor(self, qtd_litros):
        return qtd_litros * self._preco_por_litro
    
    def __str__(self):
        return f'Etanol de {self._origem}'
    
class Abastecimento:
    def __init__(self, bomba, qtd_litros):
        if isinstance(bomba, BombaDeCombustivel):
            self._bomba = bomba
        else:
            raise TypeError('Bomba inválida. A bomba deve ser do tipo BombaDeCombustivel.')
        self._combustivel = bomba._combustivel
        if isinstance(qtd_litros, (float, int)):
            if qtd_litros > 0:
                self._qtd_litros = qtd_litros
            else:
                raise ValueError('Quantidade de litros deve ser maior que zero.')
        else:
            raise TypeError('Quantidade de litros deve ser um float ou inteiro.')
        self._valor = self._combustivel.calcular_valor(qtd_litros)
        
    def resumo_abastecimento(self):
        return f'Abastecimento na bomba {self._bomba._identificador}: {self._qtd_litros} litros -> R$ {self._valor:.2f}'
    
class Controle_De_Abastecimentos:
    def __init__(self):
        self._abastecimentos = []
        self._valor_total_abastecimentos = 0
        
    def registrar_abastecimento(self, abastecimento):
        if isinstance(abastecimento, Abastecimento):
            self._abastecimentos.append(abastecimento)
            self.adicionar_valor_abastecimento(abastecimento)
            return f'Realizando abastecimento na bomba {abastecimento._bomba._identificador}: {abastecimento._qtd_litros} litros...\nTotal a pagar: R$ {abastecimento._valor:.2f}'
        else:
            raise TypeError('Abastecimento inválido. O abastecimento deve ser do tipo Abastecimento.')
        
    def resumo_abastecimentos(self):
        print('Resumo dos abastecimentos:')
        for a in self._abastecimentos:
            print(f'- Bomba {a._bomba._identificador} ({a._bomba._combustivel}): {a._qtd_litros} litros -> R$ {a._valor:.2f}')
                
    def adicionar_valor_abastecimento(self, abastecimento):
        self._valor_total_abastecimentos += abastecimento._combustivel.calcular_valor(abastecimento._qtd_litros)