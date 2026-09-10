n=int(input())
for i in range(n):
    x=input()
    l=len(x)
    if len(x)<=10:
        print(x)
    else:
        print(x[0],(len(x)-2),x[len(x)-1],sep="")
