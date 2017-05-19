# s = input()
# uu = "-"
# ll = "+"
# if "-" or "0" in s:
#     print("Оденься потеплее")
# elif "+" or "0" in s:
#     print ("Можно одеться полегче")
# else:
#     print(" ")

s = input()
integ = ''
for n in s:
    if n.isdigit():
        integ = integ + n
    else:
        integ = integ + ' '
        if "+" in s:
            ww = "+"+integ
            www = ww.replace(' ', ' ')
            print(www)
        else:
            zz = "-"+integ
            zzz = zz.replace(' ', '')