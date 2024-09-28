"""numpy indexing & slicing"""

import numpy as np

def get_column_from_bottom_to_top(A,c):
    return A[::-1,c]

def get_odd_rows(A):
    return A[1::2,:]

def get_even_column_last_row(A):
    return A[-1,::2]

def get_diagonal1(A):
    idx=np.arange(A.shape[0])
    return A[idx,idx]

def get_diagonal2(A):
    idx=np.arange(A.shape[0])
    return A[idx,idx[::-1]]

exec(input().strip())
