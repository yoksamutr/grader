"""print triangle"""

h=int(input())
base=2*h-1

for i in range(1,h+1):
    if i==1:
        print("."*(h-1)+"*")
    elif i==h:
        print("*"*base)
    else:
        line="."*(h+i-2)+"*"
        temp=line[0:h-i]+"*"+line[h-i+1:]
        print(temp)
