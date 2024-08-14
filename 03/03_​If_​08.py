"""day of year"""

def leap(num):
    if((num%4==0 and num%100!=0) or num%400==0):
        return True
    else:
        return False
    
day=int(input())
month=int(input())
year=int(input())
year-=543

days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

if(leap(year)):
    days[2]+=1

ans=0
for i in range(1,month):
    ans+=days[i]
ans+=day
print(ans)
