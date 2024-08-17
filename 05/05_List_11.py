"""missing digits"""

ip=str(input())

num=["0","1","2","3","4",
     "5","6","7","8","9"]

s={-1}
for i in ip:
    if i in num:
        s.add(int(i))

ans=[]
for j in range(10):
    if j not in s:
        ans.append(j)
        
if len(ans)==0:
    print("None")
else:
    for k in ans:
        if k==ans[-1]:
            print(k)
            continue
        print(k,end=",")
