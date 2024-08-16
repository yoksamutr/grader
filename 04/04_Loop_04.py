"""parentheses"""

ipt=str(input())

paren={"(":"[","[":"(",")":"]","]":")"}
lt=["(",")","[","]"]

ans=""
for i in ipt:
    if i in lt:
        ans+=paren[i]
        continue
    ans+=i
    
print(ans)
