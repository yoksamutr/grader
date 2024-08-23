"""queue ticket"""

_=int(input())

ans=[]
wait_list=[] #int
next_list=[] #int
time_list=[] #int
wait_index=0 #int
dt_list=[]
for e in range(_):
    order=input().split()
    if order[0]=="reset":
        n=int(order[1])
        wait_list.append(n)
    elif order[0]=="new":
        ans.append("ticket "+str(n))
        n+=1
        wait_list.append(n)
        time_list.append(int(order[1]))
    elif order[0]=="next":
        ans.append("call "+str(wait_list[wait_index]))
        next_list.append(wait_list[wait_index])
        wait_index+=1
    elif order[0]=="order":
        n1=next_list[-1] #int
        idx=wait_list.index(n1)
        dt=int(order[1])-time_list[idx]
        ans.append("qtime "+str(n1)+" "+str(dt))
        dt_list.append(dt)
    elif order[0]=="avg_qtime":
        ans.append("avg_qtime "+str(sum(dt_list)/len(dt_list)))
        
        
for answer in ans:
    print(answer)
