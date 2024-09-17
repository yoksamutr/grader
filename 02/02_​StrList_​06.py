"""add vector"""

vc1=input()[1:-1].split(", ")
vc2=input()[1:-1].split(", ")

vc1=[float(i) for i in vc1]
vc2=[float(j) for j in vc2]
ans=[vc1[e]+vc2[e] for e in range(len(vc1))]

print(vc1,"+",vc2,"=",ans)
