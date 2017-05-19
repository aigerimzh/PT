import math
s = input()
x = math.ceil(len(s)/2)
print(s[x:] + s[:x])
