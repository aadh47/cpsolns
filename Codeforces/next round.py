inp=input()
inp_sp=inp.split()
n=int(inp_sp[0])
k=int(inp_sp[1])
score=input().split()
print(score)
count=0
for i in score:
    if int(i)>=int(score[(k-1)]) and int(i) > 0:
        count+=1
print(count)