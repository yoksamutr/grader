"""Text Replace"""

old,new=input().split("/")
old=old.lower()
n=int(input())
lt=[]
for _ in range(n):
    ip=input()
    lt.append(ip)
    
sentence="\n".join(lt)
check=sentence.replace("\n"," ").lower()

idx=check.find(old)
while idx!=-1:
    sentence=sentence[:idx]+new+sentence[idx+len(old):]
    check=sentence.replace("\n"," ").lower()
    idx=check.find(old,idx+len(new))
    
print(sentence)
