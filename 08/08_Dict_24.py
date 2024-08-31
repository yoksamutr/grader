"""texting"""

l1=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

tele={" ":"0"}
for i, it in enumerate(l1):
    for j in range(len(it)):
        tele[it[j]]=str(i+2)*(j+1)
        
def text2keys(text):
    lt=[]
    for x in text:
        x=x.lower()
        if x in tele:
            lt.append(tele[x])
    return " ".join(lt)

tele2={}
for k in tele:
    tele2[tele[k]]=k

def keys2text(keys):
    ans=""
    key=keys.split()
    for x in key:
        ans+=tele2[x]
    return ans
    
exec(input().strip())
