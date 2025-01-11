class habilitacao:
    def __init__(self, cpf):
        self.cpf = cpf
        self.email = None
        self.edereco = None

def main():
    hab1 = habilitacao(1111111111)
    hab2 = habilitacao(2222222222)
    hab2.endereco = "Rua 100"

    #print(hab1.endereco)
    print(hab2.endereco)
if __name__ == '__main__':
    main()