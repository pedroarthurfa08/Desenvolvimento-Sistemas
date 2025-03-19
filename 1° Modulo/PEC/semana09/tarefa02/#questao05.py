#questao05
'''
Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima ?"
b) "Esteve no local do crime ?"
c) "Mora perto da vítima ?"
d) "Devia para a vítima ?"
e) "Já trabalhou com a vítima ?"

Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
def main():
    score = 0
    a = input("Telefonou para a vítima ?").strip()
    b = input("Esteve no local do crime ?").strip()
    c = input("Mora perto da vítima ?").strip()
    d = input("Devia para a vítima ?").strip()
    e = input("Já trabalhou com a vítima ?").strip()
    if a.upper() == "S":
        score += 1
    if b.upper() == "S":
        score += 1
    if c.upper() == "S":
        score += 1
    if d.upper() == "S":
        score += 1
    if e.upper() == "S":
        score += 1
    if score == 5:
        print("Neste crime você está sendo classificado como Assassino.")
    elif 3 <= score <= 4:
        print("Neste crime você está sendo classificado como Cúmplice.")
    elif score == 2:
        print("Neste crime você está sendo classificado como Suspeito.")
    else:
        print("Neste crime você está sendo classificado como Inocente.")
if __name__ == "__main__":
    main()