"""stirling factorial"""

import math

n=int(input())

a=(2*math.pi)**0.5
b=n**(n+0.5)
c=math.e**(-n)
d=math.e**(1/(12*n+1))
e=math.e**(1/(12*n))

ans1=a*b*c*d
ans2=a*b*c*e

print(ans1)
print(ans2)
