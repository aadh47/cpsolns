x=input().split("+")
x.sort()
y=""
for i in x:
    y+=i+"+"
print(y.rstrip("+"))
