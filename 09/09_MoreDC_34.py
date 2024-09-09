"""fill in numbers"""

def pattern1(nrows,ncols):
    if nrows==0 and ncols==0:
        return []
    elif ncols==0:
        return [[]]
    elif nrows==0:
        return []
    res=[]
    for i in range(1,nrows*ncols+1,ncols):
        res.append([e for e in range(i,i+ncols)])
    return res

def pattern2(nrows,ncols):
    res=[]
    for i in range(1,nrows+1):
        res.append([e for e in range(i,nrows*ncols+1,nrows)])
    return res

def pattern3(n):
    res=[[0]*n for _ in range(n)]
    num=1
    for i in range(n):
        for j in range(i,n):
            res[i][j]=num
            num+=1
    return res

def pattern4(n):
    res=[[0]*n for _ in range(n)]
    num=1
    for j in range(n):
        for i in range(j,-1,-1):
            res[i][j]=num
            num+=1
    return res

def pattern5(n):
    res=[[0]*n for _ in range(n)]
    num=1
    for i in range(n):
        for j in range(n):
            if i+j==n:
                break
            res[j][j+i]=num
            num+=1
    return res

def pattern6(n):
    res=[[0]*n for _ in range(n)]
    num=1
    df=n-2
    for i in range(n):
        if i%2==0:
            for j in range(n):
                if i+j==n:
                    break
                res[j][j+i]=num
                num+=1
        else:
            num+=df
            temp=num+1
            for k in range(n):
                if i+k==n:
                    break
                res[k][k+i]=num
                num-=1
            num=temp
            df-=2
    return res

exec(input().strip())
