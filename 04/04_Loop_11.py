"""RLE"""

sentence=str(input())

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

def main(s):
    lst=splitWord(s)
    ans=[]
    for x in lst:
        ans.append(x[0])
        ans.append(len(x))
    for y in ans:
        print(y,end=" ")

main(sentence)
