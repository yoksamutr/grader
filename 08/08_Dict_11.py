"""reverse and keys"""

def reverse(d):
    dic={}
    for i in d:
        dic[d[i]]=i
    return dic

def keys(d,v):
    res=[]
    for i in d:
        if d[i]==v:
            res.append(i)
    return res

exec(input().strip())
