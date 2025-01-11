'''No próximo final de semana seu time de futebol entrará em campo. Escreva um programa que leia o seu nível de empolgação para a partida, um número inteiro entre 1 e 10, e mostre a empolgação do lado de fora do estádio representando por letras “O” ao gritar GOL. Por exemplo: Empolgação nível 1 >>> Gol! Empolgação nível 5 >>> Goooool!'''
# nivelempolgacao recebe o valor inteiro
nivelempolgacao = int(input("Qual o seu nível de empolgação para o jogo de 1 a 10?"))
# s recebe a letra o e será multiplicado a nivelempolgacao
s = "o" * nivelempolgacao
print("G" + s + "l!")