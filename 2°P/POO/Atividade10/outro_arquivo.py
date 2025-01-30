def main():
    conta1 = ContaCorrente(101, "João", 1000)
    conta2 = ContaPoupanca(102, "Maria", 2000, 0.05)
    conta3 = ContaImposto(103, "Carlos", 3000, 0.02)

    print(conta1)
    conta1.creditar(500)
    print(conta1)
    conta1.debitar(200)
    print(conta1)
    
    conta1.transferir(300, conta2)
    print(conta1)
    print(conta2)
    
    conta2.renderJuros()
    print(conta2)
    
    conta3.calcula_Imposto()
    print(conta3)