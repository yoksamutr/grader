"""total play time by genre"""

n=int(input())

def tosec(t):
    m,s=[int(e) for e in t.split(":")]
    s+=m*60
    return s

def tomin(t):
    m=t//60
    s=t%60
    if s<10:
        return str(m)+":0"+str(s)
    return str(m)+":"+str(s)

dct={}
for _ in range(n):
    ip=input().split(", ")
    tp,time=ip[2],ip[3]
    if tp not in dct:
        dct[tp]=tosec(time)
    else:
        dct[tp]+=tosec(time)

temp=[]
for i,j in dct.items():
    temp.append([-j,i])
temp.sort()

if len(temp)>2:
    for k in range(3):
        print(temp[k][1],"-->",tomin(-temp[k][0]))
else:
    for l in temp:
        print(l[1],"-->",tomin(-l[0]))
