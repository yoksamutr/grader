"""positive negative"""

num=int(input())

def ps(num):
    if num>0:
        print("positive")
    elif num<0:
        print("negative")
    else:
        print("zero")

def eo(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
        
ps(num)
eo(num)
