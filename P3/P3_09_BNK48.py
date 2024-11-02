"""BNK ELECTION"""

sol1={}
temp2={}
temp3={}
sol3={}

while True:
    ip=input().split()
    if len(ip)==1:
        break
    ota,idol,vote=ip
    vote=int(vote)
    sol3[idol]=0
    if idol in sol1: #sol1
        sol1[idol]+=vote
    else:
        sol1[idol]=vote
    if idol in temp2: #sol2
        temp2[idol].add(ota)
    else:
        temp2[idol]={ota,}
    if (ota,idol) in temp3: #sol3
        temp3[(ota,idol)]+=vote
    else:
        temp3[(ota,idol)]=vote
        
def to_ans(sol):
    lt=[]
    for key,val in sol.items():
        lt.append([-val,key])
    lt.sort()
    ans=""
    for i in range(3):
        ans+=lt[i][1]+", "
    print(ans[:-2])

order=ip[0]
if order=="1":
    to_ans(sol1)
elif order=="2":
    sol2={}
    for k2,v2 in temp2.items():
        sol2[k2]=len(v2)
    to_ans(sol2)
elif order=="3":
    t3={}
    for k3,v3 in temp3.items():
        Ota,Idol,Vote=k3[0],k3[1],v3
        if Ota in t3:
            t3[Ota].append([-Vote,Idol])
        else:
            t3[Ota]=[[-Vote,Idol]]
    for val3 in t3.values():
        val3.sort()
        idl=val3[0][1]
        sol3[idl]+=1
    to_ans(sol3)
