k,  n, w = map(int, input().split())
tot=0
for i in range(1,w+1):
    tot+=(i*k)
if n<tot:
    print(tot-n)
else:
    print(0)
