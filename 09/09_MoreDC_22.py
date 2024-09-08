"""matrix multiplication"""

def read_matrix():
    m=[]
    nrows=int(input())
    for _ in range(nrows):
        r=[float(e) for e in input().split()]
        m.append(r)
    return m

def mult_c(c,a):
    ans=[]
    for i in a:
        r=[e*c for e in i]
        ans.append(r)
    return ans

def mult(a,b):
    m1,n1=len(a),len(a[0])
    n2=len(b[0])
    res=[[0]*n2 for _ in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                res[i][j]+=a[i][k]*b[k][j]
    return res
            
exec(input().strip())
