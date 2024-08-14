"""abbrevnum"""

number=int(input())
digit=len(str(number))

def round_number(num,place):
    temp=str(num)
    if(int(temp[-place+1])>=5):
        num+=10**(place-1)
    num//=(10**(place-1))
    return num

ans=0
if(digit>=10):
    if(digit==10):
        ans=round_number(number,9)
        print(str(ans/10)+"B")
    else:
        ans=round_number(number,10)
        print(str(ans)+"B")
elif(digit>=7):
    if(digit==7):
        ans=round_number(number,6)
        print(str(ans/10)+"M")
    else:
        ans=round_number(number,7)
        print(str(ans)+"M")
elif(digit>=4):
    if(digit==4):
        ans=round_number(number,3)
        print(str(ans/10)+"K")
    else:
        ans=round_number(number,4)
        print(str(ans)+"K")
else:
    print(str(number))
