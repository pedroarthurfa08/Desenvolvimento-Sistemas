class Pessoa:
  seq=0
  def __init__(self,nome,idade,peso,altura,sexo,estado="vivo",est_civil="solteiro",conjuge=None,mãe=None):
    Pessoa.seq+=1
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
    self__pai_adotivo = None
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
  def nome(self,valor):
    if self.__est_civil == "casado":
      nome_antigo = self.__nome.split(" ")
      nome_conjuge = self.__conjuge.nome.split(" ")
      novo_nome = valor.split(" ")
      for i in novo_nome:
        if (i not in nome_antigo) and (i not in nome_conjuge):
           print("nome inválido!")
           return
      self.__nome = valor
      print ("Alteração efetuada com sucesso!")

  def casar(self,conjuge):
    #verificar se as instancias estão em posições diferentes de memória
    if type(conjuge)==Pessoa:
      if self.id != conjuge.id:
        if self.__est_civil != "casado" and conjuge.__est_civil != "casado":
          self.__est_civil = "casado"
          self.__conjuge = conjuge
          self.__conjuge.__est_civil = "casado"
          self.__conjuge.__conjuge = self
          print (f'{self.__nome} casou-se com {conjuge.nome}')
      else:
        print('Pessoa não pode se casar com ela mesma!')

  def morrer(self):
    # alterar o estado para "morto"
    # verificar se a pessoa que morreu era casada e alterar o conjuge reséctivo para "viuvo"
    pass

  def divorciar(self):
    # mudar o estado civil das pessoas para "divorciado"

    pass

  def ter_filhos(self,pessoa):
    # pessoas envolvidas tem que ser de sexos opostos
    # Retornar uma nova pessoa
    # criar o vinculo

    pass

  def adotar_filhos(self,criança): #condição: criança ser órfã.
    pass

  def __str__(self):
    pass


####### execução ########

maria = Pessoa("Maria",30,65,1.7,'F', Pessoa("Francisca",65,60,1.6,'F')) # maria -> solteira
joao = Pessoa("João",25,66,170,'M') # joão -> solteiro
print(maria.id,joao.id)
maria.casar(maria)
maria.casar(joao) # joão e maria -> casado
#ana = Pessoa(...)
#pedro = joao.ter_filhos(ana)
#joao.casar(ana) # não é possivel pois joão já é casado com maria
maria.morrer() # maria para para o estado de morto.
#joao.casar(ana) # joao e ana -> casado
joao.ter_filhos(maria) # Erro! maria está morta.
#julia = ana.ter_filhos(joao)

#simular processo de adoção