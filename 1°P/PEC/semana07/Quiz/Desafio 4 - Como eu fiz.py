#Desafio 4 - Como eu fiz?

score=0

print('''
Q1 - Quanto é 1 * 10?
a - 10
b - 100
c - 1000    
 ''')
resposta=input().lower()
if resposta=="a":
    print("Correto! :)")
    score += 1 
elif resposta=="b":
    print("Errado! |:(")
elif resposta=="c":
    print("Errado! :(")
else:
    print("Tem que ser a, b ou c meu nobre? :|")

print('''
Q2 - Quanto é meia duzia?
a - 24
b - 12
c - 6
      ''')
resposta=input().lower()
if resposta=="a":
    print("Errado! :(")
elif resposta=="b":
    print("Errado! :(")
elif resposta=="c":
    print("Correto! :)")
    score += 1 
else:
    print("Tem que ser a, b ou c meu nobre? :|")

print('''
Q3 - Quanto é 2 elevado ao cubo?
a - 4
b - 6
c - 8
      ''')
resposta=input().lower()
if resposta=="a":
    print("Errado! :(")
elif resposta=="b":
    print("Errado! :(")
elif resposta=="c":
    print("Correto! :)")
    score += 1 
else:
    print("Tem que ser a, b ou c meu nobre? :|")

print('''
Q4 - Quantos segundos há em um dia?
a - 48,700 segundos
b - 64,600 segundos
c - 86,400 segundos
      ''')
resposta=input().lower()
if resposta=="a":
    print("Errado! :(")
elif resposta=="b":
    print("Errado! :(")
elif resposta=="c":
    print("Correto! :)")
    score += 1 
else:
    print("Tem que ser a, b ou c meu nobre? :|")

print('''
Q5 - Quem é o Pai da Matemática?
a - Arquimedes
b - Sócrates
c - Ritomar
      ''')
resposta=input().lower()
if resposta=="a":
    print("Correto! :)")
    score += 1 
elif resposta=="b":
    print("Errado! :(")
elif resposta=="c":
    print("Errado! :(")
else:
    print("Tem que ser a, b ou c meu nobre? :|")

if score==5:
    print("Muito bem!")
elif score<5:
    print("Tente novamente!")