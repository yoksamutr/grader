"""Text Formatting"""

fname=input().strip()
n=int(input())

line1=["-"]*n
c=1
for i in range(len(line1)):
    if (i+1)%10==0:
        line1[i]=str(c)
        c+=1
print("".join(line1))

lt=[]
fn=open(fname,"r")
for line in fn:
    line=line.strip()+"."
    w=""
    for k in range(len(line)-1):
        w+=line[k]
        if line[k]!="." and line[k+1]==".":
            if w[0]!=".":
                lt.append("."+w)
            else:
                lt.append(w)
            w=""

ans=[]
word=""
for it in lt:
    word=word.strip(".")
    if len(word)+len(it)>n:
        ans.append(word)
        word=it
    else:
        word+=it
if len(word)!=0:
    ans.append(word.strip("."))
    
print("\n".join(ans))
