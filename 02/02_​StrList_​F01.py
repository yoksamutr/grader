"""citizen id (function)"""

def check_digit(n):
    lt=[]
    for i in n:
        lt.append(int(i))
    s=0
    for j in range(12):
        s+=lt[j]*(13-j)
    n12=(11-(s%11))%10
    return n12

exec(input())
