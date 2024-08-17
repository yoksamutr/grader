"""nicknames"""

n=int(input())

lname={"Robert":"Dick","William":"Bill","James":"Jim",
       "John":"Jack","Margaret":"Peggy","Edward":"Ed",
       "Sarah":"Sally","Andrew":"Andy","Anthony":"Tony",
       "Deborah":"Debbie","Dick":"Robert","Bill":"William",
       "Jim":"James","Jack":"John","Peggy":"Margaret",
       "Ed":"Edward","Sally":"Sarah","Andy":"Andrew",
       "Tony":"Anthony","Debbie":"Deborah"}

ans=[]
for i in range(n):
    ip=str(input())
    if ip not in lname:
        ans.append("Not found")
        continue
    ans.append(lname[ip])

for j in ans:
    print(j)
