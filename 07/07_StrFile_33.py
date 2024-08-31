"""file merge"""

ip=input().split()
fn1=open(ip[0],"r")
fn2=open(ip[1],"r")

def read_next(f):
    lis=[]
    while True:
        t=f.readline()
        if len(t)==0:
            break
        id,grade=t.strip().split()
        code=id[-2::]
        lis.append([code,id,grade])
    return lis

total=read_next(fn1)+read_next(fn2)
total.sort()

for it in total:
    print(it[1],it[2])
    
fn1.close()
fn2.close()
