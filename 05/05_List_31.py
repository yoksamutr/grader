"""Cut & Shuffle"""

card=input().split()
order=input()

n=len(card)
for i in order:
    if i=="C":
        card=card[n//2:]+card[:n//2]
    elif i=="S":
        temp=[0]*n
        temp[::2]=card[:n//2]
        temp[1::2]=card[n//2:]
        card=temp
print(" ".join(card))
