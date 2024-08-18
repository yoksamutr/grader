"""upgrade"""

ids=[]
grades=[]
uids=[]

while True:
    ip=[str(e) for e in input().split()]
    if len(ip)==1:
        break
    ids.append(ip[0])
    grades.append(ip[1])
    
uids=[str(f) for f in input().split()]

change={"A":"A","B+":"A","B":"B+",
        "C+":"B","C":"C+","D+":"C",
        "D":"D+","F":"D"}

for x, it in enumerate(ids):
    if it in uids:
        print(it,change[grades[x]])
        continue
    print(it,grades[x])
