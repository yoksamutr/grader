"""US date"""

ipt=input().split("/")
d=str(ipt[0])
m=int(ipt[1])
y=str(ipt[2])

month=[0,"January","February","March",
       "April","May","June","July",
       "August","September","October",
       "November","December"]

print(month[m],d+", "+y)
