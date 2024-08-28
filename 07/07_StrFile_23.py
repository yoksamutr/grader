"""file min max average"""

ip=[str(e) for e in input().split()]
fn=open(ip[0],"r")

lt=[]
for line in fn:
    ids,score=line.split()
    year="25"+ids[:2]
    if year==ip[1]:
        lt.append(float(score))

if len(lt)==0:
    print("No data")        
else:
    print(min(lt),max(lt),sum(lt)/len(lt))

fn.close()
