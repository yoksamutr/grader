"""collatz"""

n=int(input())

ans=[]
ans.append(n)
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=3*n+1
    ans.append(n)
    
if len(ans)>15:
    ans=ans[-15:]
    for i, it in enumerate(ans):
        if i==14:
            print(it)
            continue
        print(it,end="->")
else:
    for j, it1 in enumerate(ans):
        if j==len(ans)-1:
            print(it1)
            continue
        print(it1,end="->")
