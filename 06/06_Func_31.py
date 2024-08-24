"""refactor"""

mname=[" ","Jan","Feb","Mar","Apr",
       "May","Jun","Jul","Aug","Sep",
       "Oct","Nov","Dec"]

def read_date():
    date=input().split()
    return [int(date[0]),mname.index(date[1]),int(date[2])]

def zodiac(d1,m1):
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 :
        z1 = "Aries"
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 :
        z1 = "Taurus"
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 :
        z1 = "Gemini"
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 :
        z1 = "Cancer"
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 :
        z1 = "Leo"
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 :
        z1 = "Virgo"
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 :
        z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 :
        z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 :
        z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 :
        z1 = "Capricorn"
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 :
        z1 = "Aquarius"
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 :
        z1 = "Pisces"
    return z1

def days_in_feb(y):
    if y%400==0 or (y%100!=0 and y%4==0):
        return 29
    return 28

def days_in_month(m,y):
    d30=[4,6,9,11]
    d31=[1,3,5,7,8,10,12]
    if m in d30:
        return 30
    elif m in d31:
        return 31
    else:
        return days_in_feb(y)

def days_in_between(d1,m1,y1,d2,m2,y2):
    days=0
    for i in range(12,m1-1,-1):
        days+=days_in_month(i,y1)
    days-=d1
    for j in range(1,m2):
        days+=days_in_month(j,y2)
    days+=d2
    days+=int((y2-y1-1)*365.25)
    return days

def main():
    d1,m1,y1=read_date()
    d2,m2,y2=read_date()
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())
