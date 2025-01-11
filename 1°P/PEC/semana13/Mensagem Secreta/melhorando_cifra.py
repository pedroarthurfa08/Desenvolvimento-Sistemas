import random

def embaralhar_alfabeto(alfabeto):
    alfabeto_list = list(alfabeto)
    random.shuffle(alfabeto_list)
    return ''.join(alfabeto_list)

def criptografar_mensagem(mensagem, alfabeto, chave_inicial):
    mensagem = mensagem.replace(" ", "").lower()
    alfabeto_embaralhado = embaralhar_alfabeto(alfabeto)
    mensagem_criptografada = []
    chave = chave_inicial
    
    for letra in mensagem:
        if letra in alfabeto_embaralhado:
            posicao = alfabeto_embaralhado.find(letra)
            nova_posicao = (posicao + chave) % len(alfabeto_embaralhado)
            mensagem_criptografada.append(alfabeto_embaralhado[nova_posicao])
            chave += 1
        else:
            continue
    
    return ''.join(mensagem_criptografada), alfabeto_embaralhado

def descriptografar_mensagem(mensagem, alfabeto_embaralhado, chave_inicial):
    mensagem_descriptografada = []
    chave = chave_inicial
    
    for letra in mensagem:
        if letra in alfabeto_embaralhado:
            posicao = alfabeto_embaralhado.find(letra)
            nova_posicao = (posicao - chave) % len(alfabeto_embaralhado)
            mensagem_descriptografada.append(alfabeto_embaralhado[nova_posicao])
            chave += 1
        else:
            continue
    
    return ''.join(mensagem_descriptografada)

alfabeto = "abcdefghijklmnopqrstuvwxyz"
mensagem_original = "hello world"
chave_inicial = 3

mensagem_criptografada, alfabeto_embaralhado = criptografar_mensagem(mensagem_original, alfabeto, chave_inicial)
print("Mensagem criptografada:", mensagem_criptografada)
print("Alfabeto embaralhado:", alfabeto_embaralhado)

mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, alfabeto_embaralhado, chave_inicial)
print("Mensagem descriptografada:", mensagem_descriptografada)