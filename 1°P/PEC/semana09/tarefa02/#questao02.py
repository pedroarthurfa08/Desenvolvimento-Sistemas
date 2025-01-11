#questao02
'''
Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas,
dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. Exemplos:
• 521 = cinco centenas, duas dezenas e uma unidade.
• 107 = uma centena e sete unidades.
• 80 = oito dezenas.
'''
def unidade(a):
	u = a // 1 % 10
	if u == 1:
		return 'uma unidade'
	elif u == 2:
		return 'duas unidades'
	elif u == 3:
		return 'três unidades'
	elif u == 4:
		return 'quatro unidades'
	elif u == 5:
		return 'cinco unidades'
	elif u == 6:
		return 'seis unidades'
	elif u == 7:
		return 'sete unidades'
	elif u == 8:
		return 'oito unidades'
	elif u == 9:
		return 'nove unidades'
def dezena(a):
	d = a // 10 % 10
	if d == 1:
		return 'uma dezena'
	elif d == 2:
		return 'duas dezenas'
	elif d == 3:
		return 'três dezenas'
	elif d == 4:
		return 'quatro dezenas'
	elif d == 5:
		return 'cinco dezenas'
	elif d == 6:
		return 'seis dezenas'
	elif d == 7:
		return 'sete dezenas'
	elif d == 8:
		return 'oito dezenas'
	elif d == 9:
		return 'nove dezenas'
def centena(a):
	c = a // 100 % 10
	if c == 1:
		return 'Uma centena'
	elif c == 2:
		return 'Duas centenas'
	elif c == 3:
		return 'Três centenas'
	elif c == 4:
		return 'Quatro centenas'
	elif c == 5:
		return 'Cinco centenas'
	elif c == 6:
		return 'Seis centenas'
	elif c == 7:
		return 'Sete centenas'
	elif c == 8:
		return 'Oito centenas'
	elif c == 9:
		return 'Nove centenas'
def main():
	numero = int(input("Insira um número interio que seja menor que 1000, tal número será apresentado por extenso: ").strip())
	unidades = unidade(numero)
	dezenas = dezena(numero)
	centenas = centena(numero)
	z1 = 10, 20, 30, 40, 50, 60, 80, 90
	z2= 100, 200, 300, 400, 500, 600, 700, 800, 900
	z3 = 110, 120, 130, 140, 150, 160, 170, 180, 190, 210, 220, 230, 240, 250, 260, 270, 280, 290, 310, 320, 330, 340, 350, 360, 370, 380, 390, 410, 420, 430, 440, 450, 460, 470, 480, 490, 510, 520, 530, 540, 550, 560, 570, 580, 590, 610, 620, 630, 640, 650, 660, 670, 680, 690, 710, 720, 730, 740, 750, 760, 770, 780, 790, 810, 820, 830, 840, 850, 860, 870, 880, 890, 910, 920, 930, 940, 950, 960, 970, 980, 990
	z4 = 101, 102, 103, 104, 105, 106, 107, 108, 109, 201, 202, 203, 204, 205, 206, 207, 208, 209, 301, 302, 303, 304, 305, 306, 307, 308, 309, 401, 402, 403, 404, 405, 406, 407, 408, 409, 501, 502, 503, 504, 505, 506, 507, 508, 509, 601, 602, 603, 604, 605, 606, 607, 608, 609, 701, 702, 703, 704, 705, 706, 707, 708, 709, 801, 802, 803, 804, 805, 806, 807, 808, 809, 901, 902, 903, 904, 905, 906, 907, 908, 909
	if numero >= 100 and numero <= 999 and numero not in z2 and numero not in z3 and numero not in z4:
		print(f'{centenas}, {dezenas} e {unidades}.')
	if numero in z2:
		print(f'{centenas}.')
	elif numero in z3:
		print(f'{centenas} e {dezenas}.')
	elif numero in z4:
		print(f'{centenas} e {unidades}.')
	elif numero >= 10 and numero <= 99 and numero not in z1:
		print(f'{dezenas} e {unidades}.')
	elif numero in z1:
		print(f'{dezenas}.')
	elif numero <= 9:
		print(f'{unidades}.')
if __name__ == '__main__':
	main()