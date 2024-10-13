"""File Merge"""

t1,t2=[e for e in input().split()]

fn1=open(t1,"r")
fn2=open(t2,"r")

mp={}

def maping(file):
    for line in file:
        sid,score=[x for x in line.strip().split()]
        code=sid[-2:]
        if code in mp:
            mp[code].append([sid,score])
        else:
            mp[code]=[[sid,score]]
            
maping(fn1)
maping(fn2)
        
for key,val in sorted(mp.items()):
    val.sort()
    for v in val:
        print(" ".join(v))
