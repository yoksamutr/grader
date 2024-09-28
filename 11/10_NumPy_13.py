"""logistic regression"""

import numpy as np
import math

def p(x):
    n=np.arange(x.shape[0])
    return 1/(1+math.e**(-logit(x[n,0],x[n,1])))

def logit(x0,x1):
    return -3.98+0.1*x0+0.5*x1

exec(input().strip())
