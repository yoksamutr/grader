"""flowchart01"""

a,b,c,d=[int(i) for i in input().split()]

if a>b:
    a,b=b,a
    if not d>=a:
        c+=a
    elif c>d:
        c-=a
    b=a+c+d
else:
    if c>a>=b:
        d+=a
    if d>c:
        b+=2
    else:
        b=2*b
print(a,b,c,d)
