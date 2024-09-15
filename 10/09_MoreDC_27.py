"""celebrity"""

def knows(r,x,y):
    return y in r[x]

def is_celeb(r,x):
    if len(r[x])>1:
        return False
    for i in r:
        if not knows(r,i,x) and i!=x:
            return False
    return True

def find_celeb(r):
    for c in r:
        if is_celeb(r,c):
            return c
    return None

def read_relations():
    r={}
    while True:
        d=input().split()
        if len(d)==1:
            break
        x,y=d[0],d[1]
        if x in r:
            r[x].add(y)
        if x not in r:
            r[x]={x,y}
        if y not in r:
            r[y]={y,}
    return r

def main():
    r=read_relations()
    c=find_celeb(r)
    if c==None:
        print("Not Found")
    else:
        print(c)
        
exec(input().strip())
