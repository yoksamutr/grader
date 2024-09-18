"""database"""

a=input()
b=input()
c=input()

cse=open(a,"r")
tch=open(b,"r")
data=open(c,"r")

def to_dict(txt):
    dct={}
    for i in txt:
        x,y=i.split(",")
        if "\n" in y:
            y=y.replace("\n","")
        dct[x]=y
    return dct

course=to_dict(cse)
teacher=to_dict(tch)
database=[]
for l in data:
    m,n=l.split(",")
    if "\n" in n:
        n=n.replace("\n","")
    database.append([m,n])

res=[]
for key,val in database:
    if key in course and val in teacher:
        res.append([course[key],teacher[val]])
    else:
        res.append(["record error"])

for ans in res:
    print(",".join(ans))
