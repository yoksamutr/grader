"""first fit & best fit"""

def first_fit(l,e):
    flag=True
    for i in range(len(l)):
        if sum(l[i])+e<=100:
            l[i].append(e)
            flag=False
            break
    if flag:
        l.append([e])
    return l

def best_fit(l,e):
    mx,idx=0,-1
    for i in range(len(l)):
        if sum(l[i])+e<=100:
            if sum(l[i])>mx:
                idx=i
                mx=sum(l[i])
    if idx==-1:
        l.append([e])
    else:
        l[idx].append(e)
    return l

def partition_FF(d):
    res=[[d[0]]]
    for i in range(1,len(d)):
        res=first_fit(res,d[i])
    return res

def partition_BF(d):
    res=[[d[0]]]
    for i in range(1,len(d)):
        res=best_fit(res,d[i])
    return res

exec(input().strip())
