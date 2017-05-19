s = input()

if "h" in s:
	i = s.index("h")
	if "h" in s [i + 1:]:
		rs = s[i+1:][::-1]
		j = rs.index("h")
		j = len(s) - j
		l = s[0:i]
		k = s[j:len(s)]
		print(s[0:i] + s[j:len(s)])
	else:
		print (" ")

else:
	pass
