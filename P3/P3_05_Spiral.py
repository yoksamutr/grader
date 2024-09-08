"""spiral square"""

def spiral_square(n):
    sq=[[1]*n for _ in range(n)]
    num,idx=1,0
    dt=[]
    for k in range(1,n):
        dt.append(k)
        dt.append(k)
    dt.append(n-1)
    i,j=n//2,n//2
    right,up,left,down=True,False,False,False
    while num<n**2:
        cnt=0
        if right:
            while cnt<dt[idx]:
                j+=1; num+=1; cnt+=1
                sq[i][j]=num
            right,up=False,True
        elif up:
            while cnt<dt[idx]:
                i-=1; num+=1; cnt+=1
                sq[i][j]=num
            up,left=False,True
        elif left:
            while cnt<dt[idx]:
                j-=1; num+=1; cnt+=1
                sq[i][j]=num
            left,down=False,True
        elif down:
            while cnt<dt[idx]:
                i+=1; num+=1; cnt+=1
                sq[i][j]=num
            down,right=False,True
        idx+=1
    return sq

def print_square(s):
    for i in s:
        print(" ".join([(2*" "+str(e))[-3:] for e in i]))
        
exec(input().strip())
