"""unique count"""

lt=[int(e) for e in input().split()]

s={lt[0]}
for i in lt:
    s.add(i)
    
print(len(s))

ans=[]
c=0
for it in s:
    ans.append(it)
    c+=1
    if c==10:
        break
    
print(ans)
