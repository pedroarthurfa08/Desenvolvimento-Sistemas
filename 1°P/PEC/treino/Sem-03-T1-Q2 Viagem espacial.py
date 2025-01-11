d = int(input())
v = int(input())
t = d / v
d = t // 24
d = round(d)
h = t % 24
h = round(h)
print(f'{d} dias e {h} horas')