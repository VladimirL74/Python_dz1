duration = int(input('Введите время: '))
s = duration % 60
m = (duration // 60) % 60
h = (duration // 3600) % 24
d = (duration // 3600) // 24
if d == 0 and h == 0 and m == 0:
    print(str(s) + ' сек')
elif d == 0 and h == 0:
    print(str(m) + ' мин', str(s) + ' сек')
elif d == 0:
    print(str(h) + ' час', str(m) + ' мин', str(s) + ' сек')
else:
    print(str(d) + ' дн', str(h) + ' час', str(m) + ' мин', str(s) + ' сек')
