alfabeto = "abcdefghijklmnopqrstuvwxyz"
chave = int(input("Por favor, entre com a chave de criptografia (um número inteiro): "))
letra = input("Por favor, entre com uma letra para criptografar: ")
posicao = alfabeto.find(letra)
novaPosicao = (posicao + chave) % 26
letraCriptografada = alfabeto[novaPosicao]
print("Letra criptografada:", letraCriptografada)