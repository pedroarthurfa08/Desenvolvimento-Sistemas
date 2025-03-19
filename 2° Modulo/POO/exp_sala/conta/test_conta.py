import pytest
from exp_sala.conta.contas import ContaCorrente, ContaPoupança, ContaImposto, Banco

def test_criar_conta_corrente():
    conta = ContaCorrente("123456", 1000)
    assert conta._numero == "123456"
    assert conta._saldo == 1000
    with pytest.raises(ValueError,match="Saldo inicial da conta não pode ser negativo."):
        ContaCorrente("123456", -1000)



def test_creditar_conta_corrente():
    conta = ContaCorrente("123456", 1000)
    conta.creditar(500)
    assert conta._saldo == 1500
    conta.creditar(-100)
    assert conta._saldo == 1500

def test_adicionar_contas():
    banco = Banco()
    conta1 = ContaCorrente("123456", 1000)
    conta2 = ContaPoupança("789012", 2000, 0.05)
    conta3 = ContaImposto("345678", 3000, 0.1)
    banco.adicionar_conta(conta1)
    banco.adicionar_conta(conta2)
    banco.adicionar_conta(conta3)
    assert len(banco._contas) == 3
    banco.remover_conta(conta2)
    assert len(banco._contas) == 2
    for i in banco._contas:
      assert isinstance(i,ContaCorrente) == True

