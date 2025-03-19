import outro_arquivo

class ContaCorrente:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo

    def __str__(self):
        return f"ContaCorrente({self.numero}, Titular: {self.titular}, Saldo: R$ {self._saldo:.2f})"

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente!")

    def transferir(self, valor, conta_destino):
        if valor <= self._saldo:
            self.debitar(valor)
            conta_destino.creditar(valor)
        else:
            print("Saldo insuficiente para transferência!")

    @property
    def saldo(self):
        return self._saldo


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, titular, saldo=0.0, taxa_juros=0.0):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def renderJuros(self):
        self._saldo += self._saldo * self.taxa_juros


class ContaImposto(ContaCorrente):
    def __init__(self, numero, titular, saldo=0.0, percentual_imposto=0.0):
        super().__init__(numero, titular, saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_Imposto(self):
        imposto = self._saldo * self.percentual_imposto
        self.debitar(imposto)



if __name__ == "__main__":
    outro_arquivo.main()