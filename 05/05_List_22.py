"""upgrade 2"""

ids=[]
grades=[]
uids=[]

c=0
while True:
    ip=[str(e) for e in input().split()]
    if len(ip)==1:
        break
    ids.append([int(ip[0]),c])
    grades.append(ip[1])
    c+=1
ids.sort()
    
uids=[int(f) for f in input().split()]

change={"A":"A","B+":"A","B":"B+",
        "C+":"B","C":"C+","D+":"C",
        "D":"D+","F":"D"}

for it in ids:
    if it[0] in uids:
        print(it[0],change[grades[it[1]]])
        continue
    print(it[0],grades[it[1]])
