A,B=map(int, input().split())
x=input()
if x[A]=='-' and x[:A].isdigit() and x[A+1:].isdigit():
    print("Yes")
else:
    print("No")
