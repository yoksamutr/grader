"""location analysis"""

n=int(input())

dct={} #id,city
for _ in range(n):
    sid,lst=input().split(": ")
    ids=set([e for e in lst.split(", ")])
    dct[sid]=ids
    
ans=[]
user=input()
for key,val in dct.items():
    if key!=user and len(val&dct[user])>0:
        ans.append(key)

if len(ans)==0:
    print("Not Found")
else:
    for id in ans:
        print(id)
