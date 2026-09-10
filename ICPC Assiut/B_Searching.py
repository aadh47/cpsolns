x=int(input())
y=list(map(int, input().split()))
z=int(input())
try:
    te=y.index(z)
    if y==0:
        print(0)
    else:
        print(y.index(z))
except:
    print(-1)