"""Piggy-Bank-1"""

class piggybank:
    def __init__(self):
        self.c1=0
        self.c2=0
        self.c5=0
        self.c10=0
    def add1(self,n):
        self.c1+=n
    def add2(self,n):
        self.c2+=n
    def add5(self,n):
        self.c5+=n
    def add10(self,n):
        self.c10+=n
    def __int__(self):
        t1=[self.c1,self.c2,self.c5,self.c10]
        t2=[1,2,5,10]
        total=0
        for i in range(len(t1)):
            total+=t1[i]*t2[i]
        return total
    def __lt__(self,rhs):
        return self.__int__() < rhs.__int__()
    def __str__(self):
        t1=[self.c1,self.c2,self.c5,self.c10]
        t2=[1,2,5,10]
        temp=[]
        for i in range(len(t1)):
            temp.append(str(t2[i])+":"+str(t1[i]))
        return "{"+", ".join(temp)+"}"
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
