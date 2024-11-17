"""Grader Score"""

res=[0]*9
    
def calculate():
    grader=[int(e) for e in input().split()]
    for i in range(len(grader)):
        res[i]=max(res[i],grader[i])
        
for _ in range(3):
    calculate()
    
print(sum(res))
