s = input()
s = s.split(" ")
l = []
for c in s:
	if c.isnumeric():
		l.append(int(c))
	elif c in ['*', '-', '+']:
		if len(s) < 2:
			break
		else:
			a = l.pop()
			b = l.pop()
			if c == '+':
				k = a + b
			elif c == '-':
				k = b - a
			elif c == '*':
				k = a * b
			l.append(k)
print(l[0])
