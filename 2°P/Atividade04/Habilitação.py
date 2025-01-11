class Habilitacao:
    def __init__(self, nome, org_emissor, cpf, nascimento, nome_mae, nome_pai, numero_registro):
        self.nome = nome
        self.org_emissor = org_emissor
        self.cpf = cpf
        self.nascimento = nascimento
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
        self.numero_registro = numero_registro

    def exibir_informações(self):
        print(f'Nome: {self.nome}')
        print(f'Orgão Emissor: {self.org_emissor}')
        print(f'CPF: {self.cpf}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'Nome da Mãe: {self.nome_mae}')
        print(f'Nome do Pai: {self.nome_pai}')
        print(f'Número de Registro: {self.numero_registro}')

def main():
    nome = input("Digite seu nome: ")
    org_emissor = input("Digite o Orgão Emissor: ")
    cpf = input("Digite seu CPF: ")
    nascimento = input("Digite sua data de nascimento: ")
    nome_mae = input("Digite o nome da sua mãe: ")
    nome_pai = input("Digite o nome do seu pai: ")
    numero_registro = input("Digite seu número de registro: ")

    if nome and org_emissor and cpf and nascimento and nome_mae and nome_pai and numero_registro:
        habilitacao = Habilitacao(nome, org_emissor, cpf, nascimento, nome_mae, nome_pai, numero_registro)
        habilitacao.exibir_informações()
    else:
        print("Preencha todos os campos.")

if __name__ == "__main__":
    main()