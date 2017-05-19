s = input()
integ = ''
for n in s:
    if n.isdigit():
        integ = integ + n
    else:
        integ = integ + ' '
if "+" in s:
    ww = "+"+integ
    print(ww.replace(' ', ' '))
else:
    zz = "-"+integ
    print(zz.replace(' ', ' '))
    zzz = zz.replace(' ', ' ')
    #www = ww.replace(' ', ' ')
if "-"  in zzz:
    print ("Одеться потеплее")
else:
    pass
if "+" in s:
    print ("Можно одеться полегче")
    Сейчас +1°   (18:00)
