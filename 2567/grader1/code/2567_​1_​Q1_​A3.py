"""rot90&rot180"""

h=int(input())
lt=[]
for _ in range(h):
    ip=input()
    lt.append(ip)

ipt=input()
if ipt=="rot90":
    lst=[]
    for j in range(len(lt[0])):
        temp=""
        for i in range(len(lt)-1,-1,-1):
            temp+=lt[i][j]
        lst.append(temp)
    print("\n".join(lst))
else:
    slt=[]
    for k in range(len(lt)-1,-1,-1):
        slt.append(lt[k][::-1])
    print("\n".join(slt))
