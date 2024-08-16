"""bisection log10 2"""

a=float(input())
start=0; end=0

temp=a
while temp>0:
    temp//=10
    end+=1

x=(start+end)/2
while abs(a-10**x)>(10**(-10))*max(a,10**x):
    if 10**x>a:
        end=x
    elif 10**x<a:
        start=x
    x=(start+end)/2
    
print(round(x,6))
