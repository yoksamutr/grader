"""Movie Stars"""

n=int(input())

mp={}
for _ in range(n):
    movie,n1,n2=input().split(", ")
    if n1 in mp:
        mp[n1].append(movie)
    if n2 in mp:
        mp[n2].append(movie)
    if n1 not in mp:
        mp[n1]=[movie]
    if n2 not in mp:
        mp[n2]=[movie]
        
lt=input().split(", ")
for name in lt:
    if name in mp:
        print(name,"->",", ".join(mp[name]))
    else:
        print(name,"-> Not found")
