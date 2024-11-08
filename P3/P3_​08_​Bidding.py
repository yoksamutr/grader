"""E-Bidding"""
# 80% pass T_T

n=int(input())

mp={}
mp1={}
for _ in range(n):
    ip=input().split() #code,bidder,goods,price
    tp=(ip[1],ip[2])
    if ip[0]=="B":
        mp1[tp]=int(ip[3])
        mp[ip[1]]=[0,[]]
    elif ip[0]=="W":
        if tp in mp1:
            mp1.pop(tp)

mp2={}
for key1,val1 in mp1.items(): #key1=(bidder,goods) val1=price
    if key1[1] not in mp2:
        mp2[key1[1]]=(key1[0],val1) #goods, (bidder,price)
    elif val1>mp2[key1[1]][1]:
        mp2[key1[1]]=(key1[0],val1)

for key2,val2 in mp2.items(): #key2=goods val2=(bidder,price)
    mp[val2[0]][0]+=val2[1]
    mp[val2[0]][1].append(key2)
    
for key,val in sorted(mp.items()): #key=bidder, val=[price,[goods]]
    if val[0]==0:
        print(key+": $0")
    else:
        print(key+": $"+str(val[0])+" -> "+" ".join(sorted(val[1])))
