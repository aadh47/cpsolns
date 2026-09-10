x=int(input())
y=list(map(int, input().split()))
tlist=[]
for i in y:
    if i==0:
        tlist.append(i)
    elif i<0:
        tlist.append(2)
    else:
        tlist.append(1)
for i in tlist:
    print(i,end=' ')