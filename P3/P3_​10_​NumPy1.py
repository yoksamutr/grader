"""Numpy-Functions"""

import numpy as np

def eq(a,b,p):
    pct=np.mean(a==b)*100
    if pct>=p:
        return True
    return False

def closest_point_indexes(points,p):
    pos=np.arange(points.shape[0])
    dt=(points[:,0]-p[0])**2+(points[:,1]-p[1])**2
    closest=min(dt)
    return pos[dt==closest]

def number_of_inversions(a):
    cnt=0
    for i in range(a.shape[0]):
        cnt+=np.sum(a[i]>a[i+1:])
    return cnt

exec(input().strip())
