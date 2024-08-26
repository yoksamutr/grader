"""camel case"""

string=str(input())

lt1="\'\".,()[]\\-<>;:/"
ans=""
flag=False
for i in string:
    if i==" ":
        flag=True
    elif i not in lt1:
        if flag:
            ans+=i.upper()
            flag=False
        else:
            ans+=i.lower()
    elif i in lt1:
        flag=True
ans=ans[0].lower()+ans[1:]
print(ans)
