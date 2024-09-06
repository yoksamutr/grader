"""vitamin"""

n=int(input())

show=[]
get=[]
for _ in range(n):
    ip=input().split()
    show.append(ip)
    name=ip[0] #str
    get.append(name)
    
ord=input().split()

if ord[0]=="show":
    for x in show:
        print(" ".join(x))
elif ord[1] not in get and ord[0]=="get":
    print(ord[1],"not found")
elif ord[0]=="get":
    idx=get.index(ord[1])
    print(" ".join(show[idx]))
elif ord[0]=="avg":
    ttl=0
    for it in show:
        ttl+=float(it[int(ord[1])])
    avg=ttl/n
    print(round(avg,4))
elif ord[0]=="max":
    ix=int(ord[1])
    show.sort()
    mx=0
    for c in show:
        mx=max(mx,float(c[ix]))
    for d in show:
        if float(d[ix])==mx:
            break
    print(d[0],d[ix])
else: #sort
    l=[]
    for f in show:
        l.append([float(f[int(ord[1])]),f[0]])
    l.sort()
    for g in l:
        print(g[1],end=" ")
