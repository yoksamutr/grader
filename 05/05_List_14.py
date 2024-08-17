"""peaks"""

y=[float(e) for e in input().split()]

count=0
for i in range(1,len(y)-1):
    before=y[i-1]
    cur=y[i]
    next=y[i+1]
    if cur>before and cur>next:
        count+=1
        
print(count)
