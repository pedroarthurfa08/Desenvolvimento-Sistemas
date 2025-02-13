class ContaCorrente:
  def __init__(self,numero,saldo=0):
    self._numero = numero
    if saldo < 0:
      raise ValueError("Saldo inicial da conta não pode ser negativo.")
    self._saldo = saldo

  def creditar(self,valor):
    if valor > 0:
      self._saldo += valor
    else:
      print("Valor inválido!")


  def debitar(self,valor):
    if valor > self._saldo:
      print("Saldo insuficiente!")
    else:
      self._saldo -= valor

  def transferir(self,valor,conta_destino):
    if isinstance(conta_destino) == ContaCorrente:
      if valor > self._saldo:
        print("Saldo insuficiente!")
    else:
      self.debitar(valor)
      conta_destino.creditar(valor)

  def __str__(self):
    return f"Conta nº: {self._numero}: \nSaldo R$: {self._saldo:.2f}"

class ContaPoupança(ContaCorrente):
  def __init__(self,numero,saldo,tx_juros):
    super().__init__(numero,saldo)
    self._tx_juros = tx_juros


  def render_juros(self):
    juros = self._saldo * self._tx_juros
    self.creditar(juros)

  def __str__(self):
    return super().__str__() + f"\nTx. Juros: {self._tx_juros}"

class ContaImposto(ContaCorrente):
    def __init__(self,numero,saldo,taxa_imposto):
      super().__init__(numero,saldo)
      self._taxa_imposto = taxa_imposto

    def calcula_imposto(self):
      imposto = self._saldo * self._taxa_imposto
      self.debitar(imposto)

    def __str__(self):
      return super().__str__() + f"\nTx. Imposto: {self._taxa_imposto}"

class Banco:
  def __init__(self):
    self._contas = []
    self._total_valor = 0

  def adicionar_conta(self,conta):
    if isinstance(conta,ContaCorrente):
      self._contas.append(conta)

  def remover_conta(self,conta):
    if isinstance(conta,ContaCorrente):
      self._contas.remove(conta)

  def listar_contas(self):
    for conta in self._contas:
      self._total_valor += conta._saldo
      print(conta)
    print(f'Valor total depositado: {self._total_valor}')