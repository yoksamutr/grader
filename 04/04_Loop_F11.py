"""RLE (function)"""

def splitWord(st):
    lt=[]
    st+="a"
    l=len(st)
    temp=st[0]
    for i in range(1,l):
        if st[i]==st[i-1]:
            temp+=st[i]
        else:
            lt.append(temp)
            temp=st[i]
    return lt


def RLE(t):
    lst=splitWord(t)
    ans=[]
    for x in lst:
        ans.append([x[0],len(x)])
    return ans

exec(input())
