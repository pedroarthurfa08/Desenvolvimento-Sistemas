'''A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em mil unidades.
Faça um programa que:

leia os dados da tabela pelo teclado;
leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
determine e exiba o ano de maior volume geral de vendas.
determine e exiba a média anual de vendas de cada fabricante durante o período.'''
vendas = {}

fabricantes = ["Fiat", "Ford", "GM", "Wolkswagen"]
anos = [2013, 2014, 2015, 2016, 2017, 2018]

# Coleta de dados de vendas
for fabricante in fabricantes:
    vendas[fabricante] = []
    for ano in anos:
        quantidade = int(input())
        vendas[fabricante].append(quantidade)

def fabricante_mais_vendeu(ano):
    ano_index = anos.index(ano)
    max_vendas = 0
    fabricante_top = ""
    
    for fabricante, vendas_list in vendas.items():
        if vendas_list[ano_index] > max_vendas:
            max_vendas = vendas_list[ano_index]
            fabricante_top = fabricante
    
    return fabricante_top, max_vendas

def ano_maior_volume_vendas():
    total_vendas_por_ano = [0] * len(anos)
    
    for vendas_list in vendas.values():
        for i in range(len(vendas_list)):
            total_vendas_por_ano[i] += vendas_list[i]
    
    maior_vendas = max(total_vendas_por_ano)
    ano_index = total_vendas_por_ano.index(maior_vendas)
    
    return anos[ano_index], maior_vendas

def media_anual_vendas():
    medias = {}
    
    for fabricante, vendas_list in vendas.items():
        medias[fabricante] = sum(vendas_list) / len(vendas_list)
    
    return medias

def formatar_media(media):
    """Formata a média de vendas conforme as regras especificadas."""
    if media.is_integer():
        return f"{media:.1f}"  
    else:
        media_str = f"{media:.2f}"
        return media_str.rstrip('0').rstrip('.')  

def main():
    ano_usuario = int(input())
    
    if ano_usuario in anos:
        fabricante_top, vendas_top = fabricante_mais_vendeu(ano_usuario)
        print(f"A fabricante que mais vendeu em {ano_usuario} foi a {fabricante_top} com {vendas_top} mil unidades.")
    else:
        print("Ano inválido. Por favor, digite um ano entre 2013 e 2018.")
    
    ano_max, max_vendas = ano_maior_volume_vendas()
    print(f"O ano de maior volume geral de vendas foi {ano_max} com {max_vendas} mil unidades.")
    
    medias = media_anual_vendas()
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    for fabricante, media in medias.items():
        print(f"A {fabricante} vendeu em média {formatar_media(media)} unidades por ano.")

if __name__ == "__main__":
    main()
