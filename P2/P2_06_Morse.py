"""morse code"""

def t2m(code,lt):
    res=[]
    for text in lt:
        morse=""
        flag=True
        for e in text:
            if e not in code:
                flag=False
                res.append("Invalid : "+text)
                break
            j=code.find("["+e+"]")
            j+=3
            k=code.find("[",j)
            morse+=code[j:k]+" "
        if flag:
            res.append(morse.strip())
    return res

def m2t(code,lt):
    res=[]
    for morse in lt:
        text=""
        flag=True
        for e in morse.split():
            w="]"+e+"["
            if w not in code:
                flag=False
                res.append("Invalid : "+morse)
                break
            j=code.find(w)-1
            text+=code[j]
        if flag:
            res.append(text.strip())
    return res

ip=input()
fn=open(ip,"r")

Order=fn.readline()[:-1]
Code=fn.readline()[:-1]
lst=[]
for it in fn:
    if "\n" in it:
        it=it.replace("\n","")
    lst.append(it)
    
if Order=="T2M":
    for x in t2m(Code,lst):
        print(x)
elif Order=="M2T":
    for y in m2t(Code,lst):
        print(y)
else:
    print("Invalid code")
