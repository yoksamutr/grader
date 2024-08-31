"""nicknames"""

n=int(input())

names={}
for i in range(n):
    name,nickname=input().split()
    names[name]=nickname
    names[nickname]=name
    
m=int(input())

for j in range(m):
    ask=input()
    if ask in names:
        print(names[ask])
    else:
        print("Not found")
