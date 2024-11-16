"""Electoral Votes"""

mp1={}
n1=int(input())
for _ in range(n1):
    name,vote=input().split(",")
    mp1[name]=int(vote)

mp={}   
mp2={}
n2=int(input())
for _ in range(n2):
    country,state=input().split(",")
    mp[state]=[0,0]
    mp2[country]=state
    
n3=int(input())
for _ in range(n3):
    ip=input().split(",")
    country,state=ip[:2]
    if country not in mp2:
        continue
    elif state==mp2[country]:
        mp[state][0]+=int(ip[2])
        mp[state][1]+=int(ip[3])

rep,dem=0,0
for key,val in mp.items():
    if val[0]>val[1]:
        rep+=mp1[key]
    else:
        dem+=mp1[key]
        
print(str(rep)+":"+str(dem))
if rep>dem:
    print("Republican wins")
elif rep<dem:
    print("Democrat wins")
else:
    print("Undecided")
