"""sky train"""

dct={}
while True:
    ip=input().split()
    if len(ip)==1:
        c=ip[0]
        break
    x,y=ip[0],ip[1]
    if x in dct:
        dct[x].add(y)
    if x not in dct:
        dct[x]={y,}
    if y in dct:
        dct[y].add(x)
    if y not in dct:
        dct[y]={x,}
        
if c not in dct:
    print(c)
else:
    ans=set(dct[c])
    temp=tuple(ans)
    for i in temp:
        if i in dct:
            for j in dct[i]:
                ans.add(j)
    for k in sorted(ans):
        print(k)
