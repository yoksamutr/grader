"""decimal to fraction"""

import math
a,b,c=input().split(",")

nb=len(b)
nc=len(c)

x=int(a+b+c)-int(a+b)
y=10**(nb+nc)-10**nb

divisor=math.gcd(x,y)
print(x//divisor,"/",y//divisor)
