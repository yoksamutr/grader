"""B1 Generations"""

mp={}
word="SBXYZA"
for w in word:
    mp[w]=[]

while True:
    ip=input().split()
    if ip[0]=="-1":
        break
    name,date=ip
    d,m,y=[int(e) for e in date.split("/")]
    idx=None
    if 2468<=y<=2488:
        idx=0
    elif 2489<=y<=2507:
        idx=1
    elif 2508<=y<=2523:
        idx=2
    elif 2524<=y<=2539:
        idx=3
    elif 2540<=y<=2555:
        idx=4
    elif y>=2556:
        idx=5
    mp[word[idx]].append(((y,m,d),name))

res=[]   
n=int(input())
for _ in range(n):
    od=input()
    if len(mp[od])==0:
        res.append(od+" : Not found")
    else:
        temp=[]
        mp[od].sort()
        for item in mp[od][::-1]:
            temp.append(item[1])
        res.append(od+" : "+" ".join(temp))
        
print("\n".join(res))
