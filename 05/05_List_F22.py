"""upgrade 2 (function)"""

def index_of(grades,ID):
    pos=-1
    for i, it in enumerate(grades):
        if it[0]==ID:
            pos=i
            break
    return pos
    
upg={"A":"A","B+":"A","B":"B+","C+":"B",
     "C":"C+","D+":"C","D":"D+","F":"D"}

def upgrade(grades,IDs):
    for id1 in IDs:
        for g, it in enumerate(grades):
            if id1==it[0]:
                grades[g][1]=upg[it[1]]
                break
    sortUpgrade(grades)

def sortUpgrade(arr):
    copy=sorted(arr)
    n=len(arr)
    for i in range(n):
        arr[i]=copy[i]

exec(input())
exec(input())
exec(input())
