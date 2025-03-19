class Pet:
    def __init__(self, tipo, nome, idade, peso, raca, cor, castrado=False):
        self.__tipo = tipo
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__castrado = castrado

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    def __str__(self):
        return f"{self.__tipo.capitalize()} - Nome: {self.__nome}, Idade: {self.__idade} anos, Peso: {self.__peso} kg, Raça: {self.__raca}, Cor: {self.__cor}, Castrado: {'Sim' if self.__castrado else 'Não'}"


class Pessoa:
    def __init__(self, cpf, nome, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__meus_pets = []

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    def cadastrar_pet(self, pet):
        """Adiciona um pet à lista de pets da pessoa."""
        self.__meus_pets.append(pet)
        print(f"Pet '{pet.nome}' cadastrado com sucesso!")

    def excluir_pet(self, nome):
        """Remove um pet da lista pelo nome."""
        for pet in self.__meus_pets:
            if pet.nome == nome:
                self.__meus_pets.remove(pet)
                print(f"Pet '{nome}' removido com sucesso!")
                return
        print(f"Pet '{nome}' não encontrado.")

    def mostrar_meus_pets(self):
        """Exibe a lista de pets da pessoa."""
        if not self.__meus_pets:
            print(f"{self.nome} não possui nenhum pet.")
        else:
            print(f"Pets de {self.nome}:")
            for pet in self.__meus_pets:
                print(pet)


if __name__ == "__main__":
    pessoa1 = Pessoa("12345678901", "João", "Rua das Flores, 123")
    pessoa2 = Pessoa("98765432100", "Maria", "Av. Central, 456")
    pessoa3 = Pessoa("45678912300", "Carlos", "Praça dos Sonhos, 789")

    pet1 = Pet("cachorro", "Rex", 5, 20, "Labrador", "Amarelo", True)
    pet2 = Pet("gato", "Mia", 3, 4, "SRD", "Branco", False)
    pet3 = Pet("cachorro", "Bolt", 2, 15, "Pastor Alemão", "Preto", True)

    pessoa1.cadastrar_pet(pet1)
    pessoa2.cadastrar_pet(pet2)
    pessoa3.cadastrar_pet(pet3)

    pessoa1.mostrar_meus_pets()
    pessoa2.mostrar_meus_pets()
    pessoa3.mostrar_meus_pets()

    print("\nSimulando a perda do pet 'Mia'...")
    pessoa2.excluir_pet("Mia")
    pessoa2.mostrar_meus_pets()
