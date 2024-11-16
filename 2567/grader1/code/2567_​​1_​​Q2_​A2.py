"""Positive Real Number"""

c,n=[float(e) for e in input().split()]

res=[]
for _ in range(int(n)):
    num=int(c//1)
    res.append(str(num))
    f=c-num
    if f<10**(-10):
        break
    c=1/f
    
print(", ".join(res))
