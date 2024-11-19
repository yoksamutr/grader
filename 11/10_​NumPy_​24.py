"""Peak_Indexes"""

import numpy as np

def peak_indexes(x):
    b1=x[1:-1]>x[:-2]
    b2=x[1:-1]>x[2:]
    peak=b1&b2
    pos=np.arange(1,x.shape[0]-1)
    return pos[peak]
        

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")
        
exec(input().strip())
