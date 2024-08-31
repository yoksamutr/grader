"""ice cream sales"""

n=int(input())

sales={}
for i in range(n):
    ip=input().split() #name,price
    sales[ip[0]]=int(ip[1])

m=int(input())

total=0
count={}
for j in range(m):
    name,cnt=input().split()
    if name in sales:
        total+=sales[name]*int(cnt)
        if name in count:
            count[name]+=sales[name]*int(cnt)
        else:
            count[name]=sales[name]*int(cnt)

if total==0:
    print("No ice cream sales")
else:
    res=[]
    for k in count:
        res.append([count[k]*-1,k])
    res.sort()
    top=res[0][0]
    top_sales=[]
    for l in res:
        if l[0]==top:
            top_sales.append(l[1])
        else:
            break
    print("Total ice cream sales:",float(total))
    print("Top sales:",end=" ")
    print(", ".join(top_sales))
