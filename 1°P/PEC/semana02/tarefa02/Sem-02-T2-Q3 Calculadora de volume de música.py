
'''Desenvolva um programa que peça ao usuário o nível de volume atual e o nível de volume desejado de seu aparelho de som. Calcule e mostre a diferença de volume necessária.'''
# nt recebe o valor um valor inteiro 
nt = int(input("Diga o nível de volume atual do seu aparelho:").strip())
# nd recebe o valor um valor inteiro 
nd = int(input("Diga o nível total de volume que deseja ter no seu aparelho:").strip())
# dv recebe o valor de nd subtraido o valor de nt
dv = nd - nt
# imprimi o valor de dv
print(f'A diferença entre o nível de volume atual do seu aparelho e a total é de: {dv}%')