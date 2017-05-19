s = input()

if "f" in s:
	i = s.index("f")
	if "f" in s [i + 1:]:
		rs = s[i+1:][::-1]
		j = rs.index("f")
		j = len(s) - j 
		print ("%d" % (j - 1))
	else:
		print ("-1")

else:
	print(-2)
