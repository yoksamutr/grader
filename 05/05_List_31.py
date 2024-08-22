"""cut & shuffle"""

ip=[str(e) for e in input().split()]
order=str(input())

def cut(l1):
    n=len(l1)
    return l1[n//2:]+l1[:n//2]

def shuffle(l2):
    n=len(l2)
    front=l2[:n//2]
    back=l2[n//2:]
    new=[]
    for i in range(n//2):
        new.append(front[i])
        new.append(back[i])
    return new

for ch in order:
    if ch=="C":
        ip=cut(ip)
    elif ch=="S":
        ip=shuffle(ip)
    
for ans in ip:
    print(ans,end=" ")
