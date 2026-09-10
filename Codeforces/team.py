'''n=int(input())
count=0
for i in range(n):
    local=0
    h=input().split()
    for i in h:
        if int(i)==1:
            local+=1
    if local>=2:
        count+=1
print(count)'''
n=4
for i in range(4):
    x=input()
    l=len(x)
    if len(x)<10:
        print(x)
    else:
        print(x[0],(len(x)-2),x[len(x)-1],sep="")

