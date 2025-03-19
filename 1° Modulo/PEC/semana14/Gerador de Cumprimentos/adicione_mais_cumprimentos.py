from random import *
print("Gerador de Cumprimentos")
print("----------------------")
adjetivos = [ "maravilhoso", "acima da média", "excelente", "espetacular"]
hobbies = [ "andar de bicicleta.", "programar.", "fazer chá.", "fazer o almoço" ]
nome = input("Qual o seu nome? ")
print(f"Aqui está o seu cumprimento {nome} :")
print(nome , "você é" , choice(adjetivos) , "em" , choice(hobbies) )
print("De nada!")