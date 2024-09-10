"""tiling puzzle"""

def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i
    return 0

def flatten(t):
    res=[]
    for i in t:
        for j in i:
            if j!=0:
                res.append(j)
    return res

def inversions(x):
    cnt=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                cnt+=1
    return cnt

def solvable(t):
    rn=row_number(t,0)
    flt=flatten(t)
    ivs=inversions(flt)
    if len(t)%2!=0 and ivs%2==0:
        return True
    elif len(t)%2==0:
        if ivs%2!=0 and rn%2==0:
            return True
        elif ivs%2==0 and rn%2!=0:
            return True
    return False

exec(input().strip())
