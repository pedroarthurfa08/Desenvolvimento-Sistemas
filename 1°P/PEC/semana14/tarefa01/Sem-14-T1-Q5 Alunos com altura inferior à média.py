'''Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos.'''
def obter_dados_alunos():
    alunos = []
    for i in range(30):
        nome = input().strip()
        idade = int(input().strip())
        altura = float(input().strip())
        aluno = {"nome": nome, "idade": idade, "altura": altura}
        alunos.append(aluno)
    return alunos

def calcular_media_altura(alunos):
    total_altura = 0
    for aluno in alunos:
        total_altura += aluno["altura"]
    media = total_altura / len(alunos)
    return round(media, 2)

def alunos_abaixo_da_media(alunos, media):
    abaixo_da_media = []
    for aluno in alunos:
        if aluno["idade"] > 13 and aluno["altura"] < media:
            abaixo_da_media.append(aluno)
    return abaixo_da_media

def main():
    alunos = obter_dados_alunos()
    
    media = calcular_media_altura(alunos)
    
    abaixo_da_media = alunos_abaixo_da_media(alunos, media)
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for aluno in abaixo_da_media:
        print(aluno["nome"])

if __name__ == "__main__":
    main()