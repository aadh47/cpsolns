x=int(input())
y=list(map(int, input().split()))
rev=(y[::-1])
for i in rev:
    print(i,end=" ")