"""biorhythm"""

import math

bd,bm,by,d,m,y=[int(e) for e in input().split()]

def days_in_feb(y1):
    if y1%400==0 or (y1%100!=0 and y1%4==0):
        return 29
    return 28

def days_in_month(m1,y1):
    d30=[4,6,9,11]
    d31=[1,3,5,7,8,10,12]
    if m1 in d30:
        return 30
    elif m1 in d31:
        return 31
    else:
        return days_in_feb(y1)

def days_in_between(d1,m1,y1,d2,m2,y2):
    days=0
    for i in range(12,m1-1,-1):
        days+=days_in_month(i,y1)
    days-=d1
    for j in range(1,m2):
        days+=days_in_month(j,y2)
    days+=d2
    days+=(y2-y1-1)*365
    return days

by-=543
y-=543
t=days_in_between(bd,bm,by,d,m,y)

pi=math.pi
const=2*pi*t
phy=math.sin(const/23)
emo=math.sin(const/28)
intel=math.sin(const/33)
print(t,"{:.2f}".format(phy),"{:.2f}".format(emo),
      "{:.2f}".format(intel))
