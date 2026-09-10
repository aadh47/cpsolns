name="Timur"
x=int(input())
for i in range(x):
    le=int(input())
    s=input()
    for i in s:
        if i in name and len(s)==len(name):
            var=True
        else:
            var=False
    if var==True:
        print("YES")
    else:
        print("NO")
