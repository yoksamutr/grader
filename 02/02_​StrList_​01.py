"""citizen id"""

ipt=str(input())
lst=[]
for i in ipt:
    lst.append(int(i))
    
s=0
for i in range(12):
    s+=lst[i]*(13-i)

n12=(11-(s%11))%10
lst.append(n12)

ans=""
for i in range(13):
    ans+=str(lst[i])
    if(i==0 or i==4 or i==9 or i==11):
        ans+=" "
print(ans)
