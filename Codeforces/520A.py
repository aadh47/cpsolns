import sys
le=int(input())
x=input()
l=[]
if le<26:
    print("NO")
    sys.exit()
else:
    for i in x:
        if i.lower() not in l:
            l.append(i.lower())
        else:
            pass
if len(l)==26:
    print("YES")
else:
    print("NO")