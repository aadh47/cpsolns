t=int(input())
l=input()
ls=[]
for i in l.split():
    ls.append(int(i))
hard=False
for i in ls:
    if i==1:
        hard=True
if hard==True:
    print("HARD")
else:
    print("EASY")
