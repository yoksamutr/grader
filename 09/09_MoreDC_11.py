"""leading space"""

n=int(input())

lt=[]
for _ in range(n):
    st=input()
    for i,it in enumerate(st):
        if it!=".":
            break
    lt.append("."*int(i/2)+st[i:])

for ans in lt:
    print(ans)
