import numpy as np

def sum_squares_error(y,t):
    return 0.5*np.sum((y-t)**2)

def cross_entropy_error(y,t):
    delta = 1e-7
    return -1*np.sum(t*np.log(y+delta))

y=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
t=[0,0,1,0,0,0,0,0,0]