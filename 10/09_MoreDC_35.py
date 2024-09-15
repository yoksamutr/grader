"""student info"""

n=int(input())

dct={}
for k in range(n):
    ipt=input().split()
    dct[k]=ipt
    
ans=[]    
ord=set([e for e in input().split()])
for val in dct.values():
    if set(val[1:])&ord==ord:
        ans.append(val)

if len(ans)==0:
    print("Not Found")
else:
    for i in sorted(ans):
        print(" ".join(i))
