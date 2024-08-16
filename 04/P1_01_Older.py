"""part 1 older"""

p1=[str(e) for e in input().split()]
p2=[str(f) for f in input().split()]

name1=p1[0]
name2=p2[0]
year1=int(p1[3])
year2=int(p2[3])
m1=p1[1]
m2=p2[1]
day1=int(p1[2][:-1])
day2=int(p2[2][:-1])

month={"January":1,"February":2,"March":3,"April":4,"May":5,
       "June":6,"July":7,"August":8,"September":9,
       "October":10,"November":11,"December":12}

st1=[year1,month[m1],day1]
st2=[year2,month[m2],day2]

if st1>st2:
    print(name2)
elif st1<st2:
    print(name1)
else:
    print(name1,name2)
