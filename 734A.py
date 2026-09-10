x=int(input())
win=input()
wa=0
wb=0
for i in win:
    if i=="A":
        wa+=1
    else:
        wb+=1
if wa==wb:
    print("Friendship")
elif wa>wb:
    print("Anton")
else:
    print("Danik")