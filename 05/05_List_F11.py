"""missing digits"""

def missing_digits(t):
    num=["0","1","2","3","4",
     "5","6","7","8","9"]

    s={-1}
    for i in t:
        if i in num:
            s.add(int(i))

    ans=[]
    for j in range(10):
        if j not in s:
            ans.append(j)
    return ans

exec(input())
