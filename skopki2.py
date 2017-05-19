s = input()
l = []
ok = True
for c in s:
	if c == '(' or '{' or '[':
		l.append(c)
	if c == ')' or '}' or ']':
		if len(s) <= 0:
			ok = False
			break
		k = l.pop() #last element
		if k == '(' and  c == ')':
			pass
	    elif k == '[' and  c == ']':
	    	pass
	    elif k == '{' and  c == '}':
	    	pass
	    else:
	    	ok = False
	    	break
if ok and len(l) == 0:
	print("yes")
else:
	print("no")