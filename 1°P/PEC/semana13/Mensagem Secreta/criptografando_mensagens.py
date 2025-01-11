alfabeto = "abcdefghijklmnopqrstuvwxyz"
mensagem = input("Por favor, entre com a mensagem a ser criptografa: ").lower()
mensagemCriptografada = ""
chave = input("Por favor, entre a cheva: ")
chave = int (chave)
for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(char)
        novaPosicao = (posicao + chave) % 26
        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
    else:
        mensagemCriptografada = mensagemCriptografada + char
print("Sua mensagem criptografa é: ", mensagemCriptografada)