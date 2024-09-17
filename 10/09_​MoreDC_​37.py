"""dept selection"""

n=int(input())
seat={}
for _ in range(n):
    nme,cnt=input().split()
    cnt=int(cnt)
    seat[nme]=cnt
    
m=int(input())
slt=[]
for __ in range(m):
    ip=input().split()
    ids,score,lis=ip[0],-float(ip[1]),tuple(ip[2:])
    slt.append((score,ids,lis))

ans=[]
for ls in sorted(slt):
    for major in ls[2]:
        if seat[major]>0:
            ans.append([ls[1],major])
            seat[major]-=1
            break

for st in sorted(ans):
    print(" ".join(st))
