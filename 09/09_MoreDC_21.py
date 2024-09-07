"""naive factorization"""

def factor(n):
    lt=[]
    div=2
    while n!=1:
        c=0
        while n%div==0:
            n/=div
            c+=1
        if c!=0:
            lt.append([div,c])
        div+=1
    return lt

exec(input().strip())
