"""zig zag 2"""

import math

min1=math.inf
min2=math.inf
max1=-math.inf
max2=-math.inf

i=0
while True:
    code=str(input())
    if code[0]=="Z":
        break
    a,b=code.split(' ')
    a=int(a); b=int(b)
    if i%2==0:
        min1=min(min1,a)
        max1=max(max1,b)
        min2=min(min2,b)
        max2=max(max2,a)
    else:
        min1=min(min1,b)
        max1=max(max1,a)
        min2=min(min2,a)
        max2=max(max2,b)
    i+=1
        
if code[1]=="i":
    print(min1,max1)
else:
    print(min2,max2)
