import numpy as np

def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp<=theta:
        return 0
    else:
        return 1

for i in range(2):
    for j in range(2):
        print(i,j,'AND',AND(i,j))

x=np.array([0,1])
w=np.array([0.5,0.5])
b=-0.7
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x)+b)