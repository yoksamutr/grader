"""flowchart 02"""

n,k=[int(e) for e in input().split()]

if n%2!=0:
    sum_a,sum_b,sum_c,m=0,0,0,0
    while m<k:
        a,b,c=[int(f) for f in input().split()]
        if a==b:
            if a==b==c:
                if a+b>k:
                    sum_a+=1
                    sum_b+=2
                    sum_c-=3
                else:
                    sum_a-=3
                    sum_b-=2
                    sum_c+=1
            else:
                sum_a+=2
                sum_b-=3
        m+=1
    print(sum_a,sum_b,sum_c)
else:
    s,t=[int(g) for g in input().split()]
    x=s
    y=t
    if s>t:
        x=s-t
    if s<t:
        y=2*(t-s)
    if x+y>k:
        x,y=y,x
        x=y+s**2
    print(x,y)
    
