"""scalar and array"""

import numpy as np

def toCelsius(f):
    return (f-32)*5/9

def BMI(wh):
    x=np.arange(wh.shape[0])
    return wh[x,0]/(wh[x,1]/100)**2

def distanceTo(p,points):
    x=np.arange(points.shape[0])
    p=np.array(p)
    arr=points[x]-p
    return (arr[x,0]**2+arr[x,1]**2)**0.5

exec(input().strip())
