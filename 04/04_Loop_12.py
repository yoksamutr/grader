"""zig zag 1"""

list1=[]
list2=[]

n=int(input())
for i in range(n):
    a,b=input().split()
    if i%2==0:
        list1.append(int(a))
        list2.append(int(b))
    else:
        list1.append(int(b))
        list2.append(int(a))
        
code=str(input())
if code[1]=="i":
    print(min(list1),max(list2))
else:
    print(min(list2),max(list1))
