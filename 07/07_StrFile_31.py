"""dna"""

string=input().strip().upper()
op=input()

pair={"A":"T","T":"A","C":"G","G":"C"}
atgc="ATGC"
check=False
for x in string:
    if x not in atgc:
        check=True
        break
if check:
    print("Invalid DNA")
elif op=="R":
    ans=""
    for i in string:
        ans=pair[i]+ans
    print(ans)
elif op=="F":
    freq=[0,0,0,0]
    for j in string:
        idx=atgc.find(j)
        freq[idx]+=1
    a,t,g,c=freq
    opf=["A="+str(a),"T="+str(t),"G="+str(g),"C="+str(c)]
    print(", ".join(opf))
elif op=="D":
    order=input()
    count=0
    for k in range(len(string)-len(order)+1):
        if string[k:k+len(order)]==order:
            count+=1
    print(count)
