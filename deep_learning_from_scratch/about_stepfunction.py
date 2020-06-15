import numpy as np
import matplotlib.pylab as plt
def first_step(x):
    if x>0:
        return 1
    else:
        return 0

def second_step(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0,1.0,2.0])
print(x)
y = x > 0
print(y)
print(y.astype(np.int))

def step_function(x):
    return np.array(x>0,dtype=np.int)

a = np.arange(-5.0,5.0,0.1)
b = step_function(a)
plt.plot(a,b)
plt.ylim(-0.1,1.1)
plt.show()