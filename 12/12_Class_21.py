"""Complex-Number"""

class Complex :
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        res=""
        if self.a!=0:
            res+=str(self.a)
        if self.b>0:
            if self.b==1:
                res+="+i"
            else:
                res+="+"+str(self.b)+"i"
        elif self.b<0:
            if self.b==-1:
                res+="-i"
            else:
                res+=str(self.b)+"i"
        if res=="":
            return "0"
        if res[0]=="+":
            return res[1:]
        return res
    def __add__(self, rhs):
        x=self.a+rhs.a
        y=self.b+rhs.b
        return Complex(x,y)
    def __mul__(self, rhs):
        x=(self.a*rhs.a-self.b*rhs.b)
        y=(self.a*rhs.b+self.b*rhs.a)
        return Complex(x,y)
    def __truediv__(self, rhs):
        a,b,c,d=self.a,self.b,rhs.a,rhs.b
        x=(a*c+b*d)/(c**2+d**2)
        y=(-a*d+b*c)/(c**2+d**2)
        return Complex(x,y)
    
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
