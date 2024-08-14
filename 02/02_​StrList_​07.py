"""decryption"""

ipt=str(input())

num1=0
num2=0
for i in range(32):
    x=i+1
    if(x==4 or x==11 or x==18 or x==25 or x==32):
        num1=(num1*10)+int(ipt[i])
    if(x==8 or x==13 or x==18 or x==23 or x==28):
        num2=(num2*10)+int(ipt[i])

temp=str(num1+num2+10000)
temp=temp[-4:-1]

temp=int(temp)
ans=str(temp)
code=0
while(temp>0):
    code+=temp%10
    temp//=10
code+=1
code%=10

codes={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",0:"J"}
print(ans+codes[code])
