t=int(input())
for i in range(t):
    a,b,c,d = map(int, input().split())
    if a>b or a>c or a>c:
        print(0)
    elif b>a and c>a and d>a:
        print(3)
    elif a<b and a<c 