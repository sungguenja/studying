import numpy as np
A = np.array([1,2,3,4])
B = np.array([[1,2],[3,4],[5,6]])
C = np.array([[1,2,3],[4,5,6]])
print('A')
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])
print('B')
print(B)
print(np.ndim(B))
print(B.shape)
print('B dot C = {}'.format(np.dot(B,C))) # 행렬 dot 곱셈