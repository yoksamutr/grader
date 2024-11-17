"""Class_Piggybank_2"""

class piggybank:
    def __init__(self):
        self.coins={} #key=coin value, val=number of coin
    def add(self, v, n):
        v=float(v)
        if v not in self.coins:
            self.coins[v]=0
        cnt=0
        for val in self.coins.values():
            cnt+=val
        if cnt+n>100:
            if self.coins[v]==0:
                del self.coins[v]
            return False
        else:
            self.coins[v]+=n
        return True
    def __float__(self):
        cnt=0
        for key,val in self.coins.items():
            cnt+=key*val
        return float(cnt)
    def __str__(self):
        temp=[]
        for key,val in sorted(self.coins.items()):
            temp.append(str(key)+":"+str(val))
        return "{"+", ".join(temp)+"}"
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
