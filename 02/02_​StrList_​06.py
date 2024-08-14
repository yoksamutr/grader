"""add vector"""

first=str(input())
second=str(input())
first=first[1:-1]
second=second[1:-1]

list1=list(map(float,first.split(", ")))
list2=list(map(float,second.split(", ")))
ans=[]
for i in range(3):
    ans.append(list1[i]+list2[i])
print(list1,"+",list2,"=",ans)
