"""ROT-13"""

lt=[]
apb="abcdefghijklmnopqrstuvwxyz"
apb=apb*2+apb.upper()*2
while True:
    ip=input()
    if ip=="end":
        break
    lt.append(ip)

ans=""
for x, i in enumerate(lt):
    for j in i:
        if j in apb:
            idx=apb.find(j)
            ans+=apb[idx+13]
        else:
            ans+=j
    if x<len(lt)-1:
        ans+="\n"
print(ans)
