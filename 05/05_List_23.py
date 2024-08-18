"""third closest"""

n=int(input())

lt=[]
for p in range(1,n+1):
    ip=[float(e) for e in input().split()]
    distance=(ip[0]**2)+(ip[1]**2)
    lt.append([distance,ip,p])
    
lt.sort()

it=lt[2]
print("#"+str(it[2])+": "+"("+str(it[1][0])+", "+
      str(it[1][1])+")")
