"""potpourri function"""

def convex_polygon_area(p):
    p.append([p[0][0],p[0][1]])
    front,back=0,0
    for i in range(len(p)-1):
        front+=(p[i][0]*p[i+1][1])
        back+=(p[i][1]*p[i+1][0])
    area=abs(front-back)/2
    return area

def is_heterogram(s):
    lt=[]
    for i in s:
        alp=i.lower()
        if "a"<=alp<="z":
            lt.append(alp)
    st=set(lt)
    return len(lt)==len(st)

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
    lt=[]
    for it in votes:
        lt.append([-votes[it],it])
    lt.sort()
    ans=[]
    if len(lt)<3:
        for i in lt:
            ans.append(i[1])
    else:
        for j in range(3):
            ans.append(lt[j][1])
    return ans

for k in range(2):
    exec(input().strip())
