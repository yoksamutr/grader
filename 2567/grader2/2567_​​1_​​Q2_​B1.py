"""2567_1_Quiz_2_1"""

D=[int(e) for e in input().split()]
P=sorted(D)

res=[]
cnt=0
for i in range(len(D)):
    cnt+=P[i]
    idx=cnt%len(D)
    num=D.pop(idx)
    res.append(num)
    
print(*res)
