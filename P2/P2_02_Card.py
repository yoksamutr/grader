"""card sequence"""

ip=input()

lt=[]
for i in range(0,len(ip)-1,2):
    lt.append(ip[i:i+2])

val={"A":1,"2":2,"3":3,"4":4,"5":5,
     "6":6,"7":7,"8":8,"9":9,"T":10,
     "J":11,"Q":12,"K":13}

typ={"C":1,"D":2,"H":3,"S":4}

def checkVal(a,b):
    return val[a[0]]-val[b[0]]

def checkType(a,b):
    return typ[a[1]]-typ[b[1]]

ans=[]
for i in range(len(lt)-1):
    val1=checkVal(lt[i],lt[i+1])
    val2=checkType(lt[i],lt[i+1])
    if val1>0:
        ans.append("+"+str(val1))
    elif val1<0:
        ans.append(str(val1))
    elif val2>0:
        ans.append("+"+str(val2))
    else:
        ans.append(str(val2))
        
print("".join(ans))
