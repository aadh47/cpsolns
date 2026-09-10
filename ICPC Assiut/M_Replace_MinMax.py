x=int(input())
y=list(map(int, input().split()))
low=min(y)
high=max(y)
tlist=[]
for i in y:
    if i==low:
        tlist.append(high)
    elif i==high:
        tlist.append(low)
    else:
        tlist.append(i)
for i in tlist:
    print(i, end=" ")