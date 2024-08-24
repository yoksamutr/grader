"""back n front"""

list1=[]
for i in range(int(input())):
    list1.append(int(input()))

list2=[int(e) for e in input().split()]

list3=[]
while True:
    ip3=int(input())
    if ip3==-1:
        break
    list3.append(ip3)

total=list1+list2+list3
ans=[]
flag=True
for x in total:
    if flag:
        ans.append(x)
        flag=False
    else:
        ans.insert(0,x)
        flag=True
print(ans)
