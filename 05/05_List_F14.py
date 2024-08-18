"""peaks (function)"""

def peaks(x):
    ans=[]
    for i in range(1,len(x)-1):
        if x[i]>x[i-1] and x[i]>x[i+1]:
            ans.append(i)
    return ans

exec(input())
