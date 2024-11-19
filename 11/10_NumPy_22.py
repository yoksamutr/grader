"""Outer_Product"""

import numpy as np

def mult_table(nrows,ncols):
    x=np.arange(1,nrows+1).reshape((nrows,1))
    y=np.arange(1,ncols+1)
    return x*y

exec(input().strip())
