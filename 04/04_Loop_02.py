"""bisection log10"""

a=float(input())
start=0; end=a
x=(start+end)/2

while abs(a-(10**x))>(10**(-10))*max(a,10**x):
    if 10**x>a:
        end=x
    elif 10**x<a:
        start=x
    x=(start+end)/2

print(round(x,6))
