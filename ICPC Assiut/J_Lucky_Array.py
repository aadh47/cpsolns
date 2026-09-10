x=int(input())
y=list(map(int,input().split()))
low=min(y)
c=y.count(low)
if c%2==0:
    print("Unlucky")
else:
    print("Lucky")