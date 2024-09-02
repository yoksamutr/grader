"""odd odd function"""

def is_odd(n):
    return n%2==1

def has_odds(x):
    for i in x:
        if is_odd(i):
            return True
    return False

def all_odds(x):
    for i in x:
        if not is_odd(i):
            return False
    return True

def no_odds(x):
    for i in x:
        if is_odd(i):
            return False
    return True

def get_odds(x):
    res=[]
    for i in x:
        if is_odd(i):
            res.append(i)
    return res

def zip_odds(a,b):
    l1=get_odds(a)
    l2=get_odds(b)
    idx=1
    for i in l2:
        l1.insert(idx,i)
        idx+=2
    return l1

exec(input().strip())
