s = str(input())
s = s.lower()
s = s.replace(",", "")
s = s.replace(".", "")
s = s.replace("?", "")
s = s.replace("!", "")
s = s.replace(" ", "")
ss = s[::-1]
if s == ss:
  print("Yes")
else:
  print("No")
