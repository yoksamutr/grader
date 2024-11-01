"""Gray Codes"""

n=int(input())
k=int(input())

if n<1 or k<1:
    if n<1 and k<1:
        print("Invalid n and k")
    elif n<1:
        print("Invalid n")
    else:
        print("Invalid k")
    exit(0)
    
line1=""
for num in range(1,k+1):
    str_num=str(num)
    c=(n+1)-len(str_num)
    line1+=str_num+"-"*c
line1=line1[:-1]
print(line1)

left=["0","1"]
for _ in range(n-1):
    right=left[::-1]
    for i in range(len(left)):
        left[i]="0"+left[i]
    for j in range(len(right)):
        right[j]="1"+right[j]
    left+=right
    
res=""    
for idx in range(len(left)):
    if (idx+1)%k==0:
        res+=left[idx]+"\n"
    else:
        res+=left[idx]+","
print(res[:-1])
