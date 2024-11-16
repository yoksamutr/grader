"""Card"""

class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        return "("+self.value+" "+self.suit+")"
    def getScore(self):
        val=self.value
        if val=="A": return 1
        elif val in "JQK": return 10
        else: return int(val)
    def sum(self,other):
        return (self.getScore()+other.getScore())%10
    def __lt__(self,rhs):
        lst="3,4,5,6,7,8,9,10,J,Q,K,A,2".split(",")
        i=lst.index(self.value)
        j=lst.index(rhs.value)
        return (i,self.suit) < (j,rhs.suit)
    
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    #print(Card.sum(cards[i], cards[i+1]))
    print(cards[i].sum(cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
