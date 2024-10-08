"""distance"""

def distance1(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def distance2(p1,p2):
    x1,y1,x2,y2=p1[0],p1[1],p2[0],p2[1]
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def distance3(c1,c2):
    distance=distance1(c1[0],c1[1],c2[0],c2[1])
    radius=c1[2]+c2[2]
    overlap=False
    if distance<=radius:
        overlap=True
    return distance,overlap

def perimeter(points):
    pr=0
    for i in range(len(points)-1):
        pr+=distance2(points[i],points[i+1])
    pr+=distance2(points[0],points[-1])
    return pr

exec(input().strip())
