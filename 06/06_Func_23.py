"""four functions"""

def make_int_list(x):
    ans=[]
    temp=""
    if x=="":
        return []
    for i in x:
        if i==" ":
            ans.append(int(temp))
            temp=""
        else:
            temp+=i
    ans.append(int(temp))
    return ans

def is_odd(e):
    return e%2==1

def odd_list(alist):
    ans=[]
    for i in alist:
        if is_odd(i):
            ans.append(i)
    return ans

def sum_square(alist):
    ans=0
    for i in alist:
        ans+=i**2
    return ans

exec(input().strip())
