import math

a=float(input())
b=float(input())
c=float(input())
res1=(-b-(math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
res1=round(res1,3)
res2=(-b+(math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
res2=round(res2,3)
print(res1,res2)
