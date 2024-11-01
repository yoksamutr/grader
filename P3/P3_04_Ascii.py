"""ASCII"""

txt=input()
Order=input()

lst=["LSTRIP","RSTRIP","STRIP","STRIP_ALL"]
if Order not in lst:
    print("Invalid command")
    exit(0)

fn=open(txt,"r")
lt=[e.strip() for e in fn]

num=[]
for j in range(len(lt[0])):
    check=True
    for i in range(len(lt)):
        if lt[i][j]!=".":
            check=False
            break
    if check:
        num.append(j)
if len(num)==0:
    print("\n".join(lt))
    exit(0)

#delete num
x=len(lt[0])-1
if num[0]==0:
    for l in range(len(num)-1):
        if num[l]!=num[l+1]-1:
            break
if num[-1]==x:
    for k in range(len(num)-1,0,-1):
        if num[k]!=num[k-1]+1:
            break
new=num[l:k+1]

def kuay(order):
    if order=="LSTRIP":
        if num[0]==0:
            for a in range(len(lt)):
                lt[a]=lt[a][new[0]+1:]
    elif order=="RSTRIP":
        if num[-1]==x:
            for b in range(len(lt)):
                lt[b]=lt[b][:new[-1]]
    elif order=="STRIP":
        if num[0]==0 and num[-1]==x:
            for c in range(len(lt)):
                lt[c]=lt[c][new[0]+1:new[-1]]
        elif num[0]==0:
            kuay("LSTRIP")
        else:
            kuay("RSTRIP")
    elif order=="STRIP_ALL":
        for d in range(len(lt)):
            for f in num:
                lt[d]=lt[d][:f]+" "+lt[d][f+1:]
        for g in range(len(lt)):
            lt[g]=lt[g].replace(" ","")
            
kuay(Order)
print("\n".join(lt)) 
