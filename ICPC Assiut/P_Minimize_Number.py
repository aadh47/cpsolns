x=int(input())
y=list(map(int, input().split()))
var=False
for i in range(len(y)):
    if y[i]%2!=0:
        var=False
    else:
        var=True
print(var)