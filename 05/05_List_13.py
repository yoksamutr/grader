"""Back n Front"""

n=int(input())

n1=[int(input()) for _ in range(n)]
n2=[int(e) for e in input().split()]
n3=[]
while True:
    num=int(input())
    if num==-1:
        break
    n3.append(num)
mix=n1+n2+n3

ans=[]
for i in range(len(mix)):
    if i%2==0:
        ans.append(mix[i])
    else:
        ans.insert(0,mix[i])
print(ans)
