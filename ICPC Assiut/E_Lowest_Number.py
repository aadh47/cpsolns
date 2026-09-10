x=int(input())
y=list(map(int, input().split()))
low=min(y)
print(low, y.index(low)+1)