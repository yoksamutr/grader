"""The Python"""

mp={}
sales={}
isboss=set()
notboss=set()

n=int(input())
for _ in range(n):
    noob,pro,sale=input().split(",")
    mp[noob]=pro
    sales[noob]=int(sale)
    isboss.add(pro)
    notboss.add(noob)
    
res={}
isboss-=notboss
for boss in isboss:
    res[boss]=0
    
for noob,pro in mp.items():
    temp=pro
    while temp not in isboss:
        temp=mp[temp]
    res[temp]+=sales[noob]
    
ans=[]
for key,val in res.items():
    ans.append((-val,key))

ans.sort()
for sale,name in ans:
    print("Boss "+name+" "+str(-sale))
