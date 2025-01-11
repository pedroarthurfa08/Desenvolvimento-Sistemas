from random import *
print("Gerador de Cumprimentos")
print("----------------------")
adjetivos = [ "maravilhos0", "acima da média", "excelente"]
hobbies = [ "andar de bicicleta.", "programar.", "fazer chá." ]
nome = input("Qual o seu nome? ")
print(f"Aqui está o seu cumprimento {nome} :")
print(nome , "você é" , choice(adjetivos) , "em" , choice(hobbies) )
print("De nada!")