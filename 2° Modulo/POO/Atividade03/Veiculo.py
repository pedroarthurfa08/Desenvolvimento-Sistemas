class Veiculo:
    def __init__(self, chassi, marca, modelo, ano, placa="não especifica", cor = "não especifica", proprietário = "não especifica", quilometragem = 0):
        # Atributos obrigatório
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        # Atributos não obrigatórios
        self.placa = placa
        self.cor = cor
        self.proprietário = proprietário
        self.quilometragem = quilometragem
        
    def exibir_informacoes(self):
        # Mostra informações do veículo
        print(f'Chassi: {self.chassi}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Placa: {self.placa}')
        print(f'Cor: {self.cor}')
        print(f'Proprietário: {self.proprietário}')
        print(f'Quilometragem: {self.quilometragem}')

# Captura de dados do usuário para criar um veículo
chassi = input("Digite a chassi do veículo: ")
marca = input("Digite a marca do veículo: ")
modelo = input("Digite o modelo do veículo: ")
ano = int(input("Digite o ano de fabricação do veículo: "))
placa = input("Digite a placa do veículo (ou deixe em branco para caso do carro ser zero): ") or "Carro Zero"
cor = input("Digite a cor do veículo (ou deixe em branco para 'Não especificada'): ") or "Não especificada"
proprietario = input("Digite o nome do proprietário (ou deixe em branco para 'Não especificado'): ") or "Não especificado"
quilometragem = int(input("Digite a quilometragem atual (ou deixe em branco para caso do carro ser zero): ") or 0)

def main():
    # Criação do objeto Veiculo
    veiculo = Veiculo(placa, marca, modelo, ano, cor, proprietario, quilometragem)

    # Exibe as informações do veículo
    veiculo.exibir_informacoes()
main()