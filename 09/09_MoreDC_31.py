"""primitive pythagorean triple"""

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def is_coprime(a,b,c):
    res=gcd(a,b)
    res=gcd(res,c)
    return res==1

def primitive_Pythagorean_triples(max_len):
    triple=[]
    for i in range(3,max_len):
        for j in range(i+1,max_len):
            res=pytha(i,j)
            if is_coprime(i,j,res) and res<=max_len:
                triple.append([int(res),i,j])
    triple.sort()
    for k in range(len(triple)):
        triple[k]=triple[k][1:]+[triple[k][0]]
    return triple
    
def pytha(a,b):
    c=(a**2+b**2)**0.5
    return c

exec(input().strip())
