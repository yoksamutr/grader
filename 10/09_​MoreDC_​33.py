"""polynomial"""

def to_ans(dt):
    ans=[]
    for k,v in sorted(dt.items()):
        if v!=0:
            ans.insert(0,(v,k))
    return ans

def add_poly(p1,p2):
    dct={} #degree,num
    for i in p1:
        dct[i[1]]=i[0]
    for j in p2:
        if j[1] in dct:
            dct[j[1]]+=j[0]
        else:
            dct[j[1]]=j[0]
    return to_ans(dct)

def mult_poly(p1,p2):
    dct={}
    for i in p1:
        for j in p2:
            a,b=i[0]*j[0],i[1]+j[1]
            if b in dct:
                dct[b]+=a
            else:
                dct[b]=a
    return to_ans(dct)

for _ in range(3):
    exec(input().strip())
