"""Slicing and Element-wise op"""

import numpy as np

def sum_2_rows(m):
    return m[::2,:]+m[1::2,:]

def sum_left_right(m):
    n=m.shape[1]
    return m[:,:n//2]+m[:,n//2:]

def sum_upper_lower(m):
    n=m.shape[0]
    return m[:n//2,:]+m[n//2:,:]

def sum_4_quadrants(m):
    r,c=m.shape
    return m[:r//2,:c//2]+m[r//2:,:c//2]\
        +m[:r//2,c//2:]+m[r//2:,c//2:]

def sum_4_cells(m):
    return m[::2,::2]+m[::2,1::2]\
        +m[1::2,::2]+m[1::2,1::2]

def count_leap_years(years):
    years-=543
    return sum((years%4==0)&(years%100!=0)|(years%400==0))

exec(input().strip())
