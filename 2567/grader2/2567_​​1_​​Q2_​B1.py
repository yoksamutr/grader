"""2567_1_Quiz_2_1"""

d=[int(e) for e in input().split()]
p=sorted(d)

res=[]
cnt=0
for i in range(len(d)):
    cnt+=p[i]
    idx=cnt%len(d)
    num=d.pop(idx)
    res.append(num)
    
print(*res)
