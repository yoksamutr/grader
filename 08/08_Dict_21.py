"""char count"""

word=input()

count={}
for i in word:
    i=i.lower()
    if "a"<=i<="z":
        if i not in count:
            count[i]=1
        else:
            count[i]+=1

res=[]
for j in count:
    res.append([count[j]*-1,j])
res.sort()

for k in res:
    print(k[1],"->",k[0]*-1)
