import numpy as np

def AND(x1,x2):
    X = np.array([x1,x2])
    W = np.array([0.5,0.5])
    b=-0.7
    tmp = np.sum(X*W)+b
    if tmp<=0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    X = np.array([x1,x2])
    W = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(X*W)+b
    if tmp<=0:
        return 0
    else:
        return 1

def OR(x1,x2):
    X = np.array([x1,x2])
    W = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(X*W) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    X_or1 = NAND(x1,x2)
    X_or2 = OR(x1,x2)
    result = AND(X_or1,X_or2)
    return result
    
x=np.array([0,1])
w=np.array([0.5,0.5])
b=-0.7
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x)+b)