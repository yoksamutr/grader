"""cut & shuffle"""

ip=[str(e) for e in input().split()]
order=str(input())

def cut(l1):
    front=[]
    back=[]
    for i, it1 in enumerate(l1):
        if (i+1)*2<=len(l1):
            back.append(it1)
        else:
            front.append(it1)
    return front+back

def shuffle(l2):
    front=[]
    back=[]
    for j, it2 in enumerate(l2):
        if (j+1)*2<=len(l2):
            front.append(it2)
        else:
            back.append(it2)
         
    new=[]   
    for k, it in enumerate(front):
        new.append(it)
        new.append(back[k])
    return new

for ch in order:
    if ch=="C":
        ip=cut(ip)
    elif ch=="S":
        ip=shuffle(ip)
    
for ans in ip:
    print(ans,end=" ")
