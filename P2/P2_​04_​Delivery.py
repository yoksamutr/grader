"""delivery"""

def invalid_year(y):
    if y>=2558:
        return False
    return True

def leap(y):
    day_in_month=[0,31,28,31,30,31,30,31,
              31,30,31,30,31]
    y-=543
    if (y%400==0) or (y%4==0 and y%100!=0):
        day_in_month[2]=29
    return day_in_month

def invalid_date(d,m,y):
    day_in_month=leap(y)
    if 1<=d<=day_in_month[m]:
        return False
    return True

def invalid_month(m):
    if 1<=int(m)<=12:
        return False
    return True

def invalid_delivery_type(ch):
    if ch in "EQNF":
        return False
    return True

def newdate(ch,d,m,y):
    day_in_month=leap(y)
    time={"E":1,"Q":3,"N":7,"F":14}
    d+=time[ch]
    if d>day_in_month[m]:
        d-=day_in_month[m]
        m+=1
    if m>12:
        y+=1
        m=1
    return [y,m,d]

ans=[]
temp=[]
while True:
    ip=input()
    if ip=="END":
        break
    error="Error: "+ip+" --> "
    sid,ord,day,month,year=ip.split()
    day,month,year=int(day),int(month),int(year)
    if invalid_year(year):
        ans.append(error+"Invalid year")
    elif invalid_month(month):
        ans.append(error+"Invalid month")
    elif invalid_date(day,month,year):
        ans.append(error+"Invalid date")
    elif invalid_delivery_type(ord):
        ans.append(error+"Invalid delivery type")
    else:
        temp.append([newdate(ord,day,month,year),sid])

for i in ans:
    print(i)
temp.sort()
for it in temp:
    date=[str(e) for e in it[0]][-1::-1]
    print(it[1]+": delivered on "+"/".join(date))
