"""bowling"""

result=input().strip()
target=int(input())
i=0
total_score=0
list_score=[]

lt=[]
for it in result:
    if it=="X":
        lt.append(10)
    elif it=="/":
        lt.append(it)
    else:
        lt.append(int(it))

each_score=0
for f in range(1,10): #frame 1-9
    if lt[i]==10:
        each_score+=10
        i+=1
        if lt[i+1]=="/":
            each_score+=10
        else:
            each_score+=lt[i]+lt[i+1]
    elif lt[i+1]=="/":
        each_score+=10
        i+=2
        each_score+=lt[i]
    else:
        each_score+=lt[i]+lt[i+1]
        i+=2
    list_score.append(each_score)
    total_score+=each_score
    each_score=0
    
if lt[i]==10: #frame 10
    each_score+=10
    if lt[i+2]=="/":
        each_score+=10
    else:
        each_score+=lt[i+1]+lt[i+2]
elif lt[i+1]=="/":
    each_score+=10+lt[i+2]
else:
    each_score+=lt[i]+lt[i+1]
list_score.append(each_score)
total_score+=each_score
list_score.insert(0,total_score)

if 0<=target<=10:
    print(list_score[target])
else:
    print(total_score)
    
