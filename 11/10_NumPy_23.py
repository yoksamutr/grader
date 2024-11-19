"""Lower_than_Mean"""

import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight,data):
    npy=np.sum(weight*data[:,1:],axis=1)
    mn=np.mean(npy)
    ids=data[:,0]
    res=ids[npy<mn]
    res=[str(s) for s in res]
    if len(res)==0:
        print("None")
    else:
        print(", ".join(res))

exec(input().strip())
