#l = []
#last in last out 
#stack overflow
#l.append(1)
#l.pop()
#len(l)
s = input()
l = []
ok = False
for c in s:
	if c == '(' or ')':
		l.append(c)
	if c == ')' or '(':
		if len(s) > 0:
				l.pop()
		else:
			ok = False
	if c == '[':
		l.append(c)
	if c == ']':
		if len(s) > 0:
				l.pop()
		else:
			ok = False
	if c == '{':
		l.append(c)
	if c == '}':
		if len(s) > 0:
				l.pop()
		ok = False
if len(l) == 0:
    print("yes")
else:
    print("no")

