"""union & intersection"""

n=int(input())

if n==0:
    print(0)
    print(0)
else:
    ans1=set([int(a) for a in input().split()])
    ans2=ans1

    for _ in range(n-1):
        lst=set([int(e) for e in input().split()])
        ans1=ans1|lst
        ans2=ans2&lst
    
    print(len(ans1))
    print(len(ans2))
