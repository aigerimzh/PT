s = "Kbtu"
n = len(s) # s.size()
print(s[0]) # >>> K
print(s[-1]) # >>> u
print(s[:2]) # >>> Kb
print(s[-2:]) # >> tu
#s[1] = 'u'
# String is ummutable 
s = s.replace('b', 'u')

s = 'Hello world'
for symbol in s:
	print(ord(symbol)) #ord ascii code
s = 'KBTU, SDU, IITU, KIMEP'
l = s.split(",")
ll = []
for item in l:
	ll.append(item.replace(' ', ''))  # remove odd spaces
lll = "\t".join(ll)
print(lll)
reversed_s = s[::-1]
s = 'Hello world'
if s.startswith("Hello"):
	print("yes")
if s.endswith("old"):
	print("Yes")

s = s + "!"




