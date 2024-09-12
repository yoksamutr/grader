"""winner"""

n=int(input())

winner={}
for _ in range(n):
    w,l=input().split()
    if w not in winner:
        winner[w]=1
    winner[l]=0

ans=[name for name,num in winner.items() if num==1]
print(sorted(ans))
