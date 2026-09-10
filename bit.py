x=0
n=int(input())
for i in range(n):
    X=input()
    if X not in ["X++","++X", "--X", "X--"]:
        break
    else:
        if X=="++X" or X=="X++":
            x=x+1
        elif X=="--X" or X=="X--":
            x=x-1
print(x)