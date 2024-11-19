"""scalar and array"""

import numpy as np

def toCelsius(f):
    return (f-32)*5/9

def BMI(wh):
    return wh[:,0]/(wh[:,1]/100)**2

def distanceTo(p,points):
    dx=p[0]-points[:,0]
    dy=p[1]-points[:,1]
    return (dx**2+dy**2)**0.5

exec(input().strip())
