"""compound interest"""

ipt=input().split()
birth_month=[int(e) for e in ipt[0].split("/")][1]
money=int(ipt[1])
cnt_month=int(ipt[2])
cur_month=int(ipt[3])

prof=[4,1,2,3]
mth=[12,1,2,3,4,5,6,7,8,9,10,11]
for i in range(1,cnt_month+1):
    profit=prof[i%4]
    if mth[cur_month%12]==birth_month:
        profit+=1
    money+=(profit/100)*(1/12)*money
    cur_month+=1
    
print(round(money,2))
