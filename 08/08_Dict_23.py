"""telephone dictionary"""

n=int(input())

teledict={}
for i in range(n):
    fname,lname,number=input().split()
    fullname=fname+" "+lname
    teledict[fullname]=number
    teledict[number]=fullname
    
m=int(input())
search=[]
for j in range(m):
    s=input()
    search.append(s)
    
for it in search:
    if it in teledict:
        print(it,"-->",teledict[it])
    else:
        print(it,"--> Not found")
