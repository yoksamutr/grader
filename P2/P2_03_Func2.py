"""potpourri"""

def convex_polygon_area(p):
    p.append(p[0])
    n1,n2=0,0
    for i in range(len(p)-1):
        n1+=p[i][0]*p[i+1][1]
        n2+=p[i][1]*p[i+1][0]
    return abs(n1-n2)/2

def is_heterogram(s):
    mp={}
    for i in s.lower():
        if "a"<=i<="z":
            if i in mp:
                return False
            else:
                mp[i]=0
    return True

def replace_ignorecase(s,a,b):
    copy=s.lower()
    idx=[]
    x=copy.find(a.lower())
    while True:
        idx.append(x)
        x=copy.find(a.lower(),x+len(a))
        if x==-1:
            break
    ans=""
    i=0
    while i<len(s):
        if i in idx:
            ans+=b
            i+=len(a)
        else:
            ans+=s[i]
            i+=1
    return ans

def top3(votes):
    temp=[]
    for key,val in votes.items():
        temp.append([-val,key])
    temp.sort()
    ans=[name for vote,name in temp]
    if len(ans)>3:
        return ans[:3]
    return ans

for k in range(2):
    exec(input().strip())
