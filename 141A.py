x=input()
y=input()
z=input()
st=x+y+z
l=0
for i in st:
    if i.lower() in "newyardchistm":
        l+=1
    else:
        pass
if l==13:
    print("YES")
else:
    print("NO")