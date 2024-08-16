"""golf score"""

import math

lpar=[]
lstroke=[]
ladj=[]

for i in range(9):
    par,stroke,choose=[int(e) for e in input().split()]
    lpar.append(par)
    lstroke.append(stroke)
    if choose==1:
        ladj.append(min(par+2,stroke))

spar=sum(lpar)
sstroke=sum(lstroke)
sadj=sum(ladj)

handicap=math.floor(0.8*(1.5*sadj-spar))
total=sstroke-handicap

print(sstroke)
print(handicap)
print(total)
