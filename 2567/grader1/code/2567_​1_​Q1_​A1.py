"""flowchart"""

a,b,c,d=[int(x) for x in input().split()]

if a==1:
    a=b+c+d
    if b==1:
        c+=c+d
    elif b==2:
        c+=c-d
    else:
        if b>4:
            c+=c*d
        if b>5:
            c+=c%d
        else:
            c+=c//d
    print(c)
else:
    while b<c:
        b+=1
        if b>a:
            break
        c-=1
        if a>d:
            break
        a+=c
print(a,b,c,d)
