# Na primeira parte do código temos um função que removerá os acentos das palavras
def remover_acentos(texto):
    from unicodedata import normalize
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

# Na segunda parte do código temos um função que formatará a data que o usuário irá inserir.
def separar_data(dma):
    a = dma % 10000
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma
    return d, m, a

# A terceira parte do código foi definida uma função para identificar o signo do usuário de acordo com o dia mês de nascimento do usuário.
def signo(dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Aries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gemeos'
    if mes == 6:
        return 'Gemeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leao' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpiao' if dia < 22 else 'Sagitario'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquario'
    if mes == 2:
        return 'Aquario' if dia < 19 else 'Peixes'

# Na segunda parte do código temos uma função que lerá o signo do usuário e abrir o site do horócopo virtual e será apresntado a frase do dia do signo; Será definido também onde o teto começa e onde ele termina
def horoscopo(signo_desejado):
    import urllib.request

    signo_formatado = remover_acentos(signo_desejado).lower()
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    resposta = urllib.request.urlopen(requisicao)
    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final]

# Na quinta função do código será colocado a entrada de dados, onde será processado nas funções 'signo(dia, mes)'; 'horoscopo(meu_signo)'; 'separar_data(nascimento)' e terá como saida a função horoscopo_de_hoje.
def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saída de dados
    print(horoscopo_de_hoje)

if __name__ == '__main__':
    main()