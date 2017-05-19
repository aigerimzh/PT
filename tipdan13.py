s = input()
 
if "h" in s:
    i = s.index("h")
    if "h" in s [i + 1:]:
        rs = s[i+1:][::-1]
        j = rs.index("h")
        j = len(s) - j
        u = s[i+2:j-1]
 
        print(s[0:i+2] + u.replace("h", "H")+ s[j-1:len(s)])
    else:
        print (" ")
 
else:
    pass
 

