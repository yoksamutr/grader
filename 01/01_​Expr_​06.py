"""duration"""

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
dt=(86400+(t2-t1))%86400
dh=dt//3600
dt%=3600
dm=dt//60
ds=dt%60
print(str(dh)+":"+str(dm)+":"+str(ds))
