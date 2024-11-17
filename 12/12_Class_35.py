"""Class_Roman_Numerals"""

class roman :
    def __init__(self, r):
        self.r=r
    def __lt__(self, rhs):
        return self.__int__() < rhs.__int__()
    def __str__(self):
        num=self.__int__()
        value_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res=""
        for val,roman in value_to_roman:
            while num>=val:
                res+=roman
                num-=val
        return res
    def __int__(self):
        word=self.r
        string="I, V, X, L, C, D, M".split(", ")
        number=[1, 5, 10, 50, 100, 500, 1000]
        mp={}
        for idx in range(len(string)):
            mp[string[idx]]=number[idx]
        res=0
        for i in range(len(word)-1):
            if string.index(word[i])<string.index(word[i+1]):
                res-=mp[word[i]]
            else:
                res+=mp[word[i]]
        res+=mp[word[-1]]
        return res
    def __add__(self, rhs):
        return self.__int__()+rhs.__int__()
    
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(roman.__str__(a+b))
