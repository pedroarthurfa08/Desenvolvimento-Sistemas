class Pessoa:
    seq = 0

    def __init__(self, nome, idade, peso, altura, sexo, estado="vivo", est_civil="solteiro", conjuge=None):
        Pessoa.seq += 1
        self.__id = Pessoa.seq
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__mãe = None
        self.__pai = None
        self.__mãe_adotiva = None
        self.__pai_adotivo = None
        self.__conjuge = None
        self.filhos = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def conjuge(self):
        return self.__conjuge

    @property
    def est_civil(self):
        return self.__est_civil

    @nome.setter
    def nome(self, valor):
        if self.__est_civil == "casado":
            nome_antigo = self.__nome.split(" ")
            nome_conjuge = self.__conjuge.nome.split(" ")
            novo_nome = valor.split(" ")
            for i in novo_nome:
                if (i not in nome_antigo) and (i not in nome_conjuge):
                    print("Nome inválido!")
                    return
            self.__nome = valor
            print("Alteração efetuada com sucesso!")

    def casar(self, conjuge):
        if type(conjuge) == Pessoa:
            if self.id != conjuge.id:
                if self.__est_civil not in ["casado"] and conjuge.__est_civil not in ["casado"]:
                    self.__est_civil = "casado"
                    self.__conjuge = conjuge
                    conjuge.__est_civil = "casado"
                    conjuge.__conjuge = self
                    print(f'{self.__nome} casou-se com {conjuge.nome}')
                else:
                    print("Uma das pessoas já está casada e não pode casar novamente!")
            else:
                print("Pessoa não pode se casar com ela mesma!")

    def morrer(self):
        self.__estado = "morto"
        if self.__est_civil == "casado":
            self.__conjuge.__est_civil = "viúvo"
            self.__conjuge.__conjuge = None
        print(f"{self.__nome} está agora morto(a).")

    def divorciar(self):
        if self.__est_civil == "casado":
            self.__conjuge.__est_civil = "divorciado"
            self.__conjuge.__conjuge = None
            self.__est_civil = "divorciado"
            self.__conjuge = None
            print("O casal agora está divorciado.")
        else:
            print("A pessoa não está casada!")

    def ter_filhos(self, parceiro):
        if self.__sexo == "Feminino" and parceiro.__sexo == "Masculino":
            filho = Pessoa(
                nome=f"Filho de {self.__nome} e {parceiro.nome}",
                idade=0,
                peso=3.5,
                altura=50,
                sexo="Masculino" if Pessoa.seq % 2 == 0 else "Feminino"
            )
            filho.__pai = parceiro
            filho.__mãe = self
            self.filhos.append(filho)
            parceiro.filhos.append(filho)
            print(f"{self.__nome} e {parceiro.nome} tiveram um filho(a): {filho.nome}")
            return filho
        else:
            print("Condições para ter filhos não atendidas! Apenas uma mulher pode ter filhos com um homem.")

    def adotar_filhos(self, crianca):
        if crianca.__mãe is None and crianca.__pai is None:
            crianca.__mãe_adotiva = self if self.__sexo == "Feminino" else crianca.__mãe_adotiva
            crianca.__pai_adotivo = self if self.__sexo == "Masculino" else crianca.__pai_adotivo
            self.filhos.append(crianca)
            print(f"{self.__nome} adotou {crianca.nome}")
        else:
            print("A criança não é órfã e não pode ser adotada!")

    def __str__(self):
        return f"Pessoa: {self.__nome}, Idade: {self.__idade}, Sexo: {self.__sexo}, Estado Civil: {self.__est_civil}"
