'''Você é um aprendiz de feiticeiro encarregado de preparar uma poção mágica especial. Para isso, você precisa de porções dos ingredientes mágicos Pó de Lua Estelar, Essência de Dragão e Lágrimas de Fênix. No entanto, cada ingrediente tem um preço diferente no mercado mágico. O ingrediente Pó de Lua Estelar custa 5 moedas de ouro por porção, Essência de Dragão custa 3 moedas de ouro por porção, e o Lágrimas de Fênix custa 8 moedas de ouro por porção. O programa deve começar perguntando quantas porções de cada ingrediente são necessárias para a poção que você está preparando. Depois, o programa deve calcular o custo total baseado na quantidade de cada ingrediente e seus respectivos preços. Finalmente, o programa deve mostrar o custo total para preparar a poção. Por exemplo, se a porção tem 2 Pó de Lua Estelar, 3 Essência de Dragão e 1 Lágrima de Fênix o custo total será: (2 * 5) + (3 * 3) + (1 * 8) = 27 (o custo total será de 27 moedas de ouro)'''
# pó_estela tem o valor igual a 5
pó_estelar = (5)
# essência_dragão tem o valor igual a 3
essência_dragão = (3)
# lágrima_fênix tem o valor iguala 8
lágrima_fênix = (8)
# imprime a frase: 0Bom dia meu nobre!
print("Bom dia meu nobre!")
# qnt_pó_estelar recebe um valor inteiro
qnt_pó_estelar = int(input("Qual a quantidade da porção de Pó de Lua Estelar? "))
# vt_pó_de_lua_estela recebe o valor de pó_estelar que será multiplicado por qnt_pó_estelar
vt_pó_de_lua_estela = pó_estelar * qnt_pó_estelar
# qnt_essência_dragão recebe um valor inteiro
qnt_essência_dragão = int(input("Qual a quantidade de porção de Essênia de Dragão? "))
# vt_essência_dragão recebe o valor de essência_dragão que será multiplicado por qnt_essência_dragão
vt_essência_dragão = essência_dragão * qnt_essência_dragão
# qnt_lágrima_fênix recebe um valor inteiro
qnt_lágrima_fênix = int(input("Qual a quantidade da porção de lágrimas de Fênix? "))
# vt_lágrima_fênix recebe o valor de lágrima_fênix que será multiplicado por qnt_lágrima_fênix
vt_lágrima_fênix = lágrima_fênix * qnt_lágrima_fênix
# valor_total recebe o valor de vt_essência_dragão somado ao vt_pó_de_lua_estela e somado vt_lágrima_fênix
valor_total = vt_essência_dragão + vt_pó_de_lua_estela + vt_lágrima_fênix
# imprime o valor total
print(f'O custo total da sua compra será de {valor_total} moedas de ouro.')