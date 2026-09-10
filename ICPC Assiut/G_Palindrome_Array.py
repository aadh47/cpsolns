x=int(input())
y=list(map(int, input().split()))
rev=y[::-1]
if y==rev:
    print("YES")
else:
    print("NO")