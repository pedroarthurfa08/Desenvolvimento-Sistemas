class ContaBancaria:
    def __init__(self, titular, saldo=0, limite=0):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= self.__saldo + self.__limite:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def mostrar_saldo(self):
        print(f"Titular: {self.__titular} | Saldo: R${self.__saldo:.2f} | Limite: R${self.__limite:.2f}")


# Testando a classe ContaBancaria
if __name__ == "__main__":
    print("--- Teste Conta 1 ---")
    conta1 = ContaBancaria("João", saldo=1000, limite=500)
    conta1.mostrar_saldo()
    conta1.depositar(200)
    conta1.sacar(300)
    conta1.sacar(1500)

    print("\n--- Teste Conta 2 ---")
    conta2 = ContaBancaria("Maria", saldo=500, limite=200)
    conta2.mostrar_saldo()
    conta2.sacar(600)
    conta2.depositar(100)
    conta2.sacar(200)

    print("\n--- Teste Conta 3 ---")
    conta3 = ContaBancaria("Carlos", saldo=0, limite=100)
    conta3.mostrar_saldo()
    conta3.sacar(50)
    conta3.depositar(300)
    conta3.sacar(350)
