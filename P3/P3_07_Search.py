"""Search Engine"""

n=int(input())

mp={}
for _ in range(n):
    name=input()
    stn=input().split()
    mp[name]=(stn,len(stn),len(set(stn)))
    
ans=[]
while True:
    word=input()
    if word=="-1":
        break
    lt=[]
    for i in mp:
        cnt=0
        for j in mp[i][0]:
            if word==j:
                cnt+=1
        if cnt==0:
            continue
        score=(cnt/mp[i][1])/mp[i][2]
        lt.append([score,i])
    if len(lt)==0:
        ans.append("NOT FOUND")
    else:
        lt.sort()
        ans.append(lt[-1][1])
        
print("\n".join(ans))
