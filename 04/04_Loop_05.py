"""count word"""

word=str(input())
sentence=str(input())

def remove(a):
    t=""
    op=["\"","(",")",",",".","\'"]
    for x in a:
        if x in op:
            t+=" "
        else:
            t+=x
    return t
    
def to_list(s):
    s=remove(s)
    list1=[]
    temp=""
    for i in s:
        if i==" ":
            list1.append(temp)
            temp=""
        else:
            temp+=i
    list1.append(temp)
    return list1

def main(w,st):
    count=0
    lt=to_list(st)
    for y in lt:
        if w==y:
            count+=1
    print(count)

main(word,sentence)
