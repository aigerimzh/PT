a=input()
s=str()
j=0
for i in a:
    if j%3==0:
        j+=1 #1 
    else:
        s+=i 
        j+=1
print(s)
