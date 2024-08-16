"""RLE"""

code=str(input())

def splitWord(w):
    lst=[]
    w+=" "
    temp=w[0]
    for x in range(1,len(w)):
        if w[x]==w[x-1]:
            temp+=w[x]
            continue
        lst.append(temp)
        temp=w[x]
    return lst

def rle(word):
    lis=splitWord(word)
    ls=[]
    for y in lis:
        ls.append(y[0])
        ls.append(len(y))
    for z in ls:
        print(z,end=" ")
      
if code=="str2RLE":
    ip1=str(input())
    rle(ip1)
elif code=="RLE2str":
    lt=[str(e) for e in input().split()]
    for i in range(0,len(lt),2):
        t=int(lt[i+1])
        print(lt[i]*t,end="")
else:
    print("Error")
