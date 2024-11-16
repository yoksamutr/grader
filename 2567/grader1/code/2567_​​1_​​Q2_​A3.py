"""hor_flip & ver_flip"""

n=int(input())

lt=[]
for _ in range(n):
    ip=input()
    lt.append(ip)
    
order=input()
if order=="hflip":
    for w in lt:
        print(w[::-1])
elif order=="vflip":
    for i in range(len(lt)-1,-1,-1):
        print(lt[i])
