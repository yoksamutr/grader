"""Giant Checker"""

pos=input().strip()

row=""
col=""
if len(pos)==1:
    print("Invalid column")
    exit()
elif len(pos)<=3: #v1
    row=pos[0]
    col=pos[1:]
else: #v2
    t1,t2=pos.split(",")
    t1,t2=t1.strip().split("="),t2.strip().split("=")
    row=t1[1].strip()
    col=t2[1].strip()
    if t1[0].strip()=="col":
        row,col=col,row

def bw(r,c):
    check="abcdefghijklmnopqrstuvwxyz"
    check+=check.upper()
    num=[int(e) for e in range(1,53)]
    idx1=check.find(r)
    idx2=num.index(int(c))
    if (idx1+idx2)%2==0:
        print("White")
    else:
        print("Black")

def invalid_row(r):
    if len(row)>1:
        return True
    check="abcdefghijklmnopqrstuvwxyz"
    check+=check.upper()
    if r in check:
        return False
    return True

def invalid_column(c):
    if len(c)==0 or len(c)>2:
        return True
    check=" 0123456789"
    for i in c:
        if i not in check:
            return True
    if 1<=int(c)<=52:
        return False
    return True

if invalid_row(row) or invalid_column(col):
    if invalid_row(row) and invalid_column(col):
        print("Invalid row and column")
    elif invalid_row(row):
        print("Invalid row")
    else:
        print("Invalid column")
else:
    bw(row,col)
