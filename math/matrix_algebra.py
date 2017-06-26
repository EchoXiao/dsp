# Matrix Algebra

import numpy as np
from numpy import linalg as LA

A = np.array([[1, 2, 3], [2, 7 ,4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])

#Q1
print('Dimension of A is: %s by %s' % (A.shape[0], A.shape[1]))
print('Dimension of B is: %s by %s' % (B.shape[0], B.shape[1]))
print('Dimension of C is: %s by %s' % (C.shape[0], C.shape[1]))
print('Dimension of D is: %s by %s' % (D.shape[0], D.shape[1]))
print('Dimension of u is: %s by %s' % (u.shape[0], u.shape[1]))
print('Dimension of v is: %s by %s' % (v.shape[0], v.shape[1]))
print('Dimension of w is: %s by %s' % (w.shape[0], w.shape[1]))

#Q2
print('u+v is:', sum(u, v))
print('u-v is:', u - v)
print('alpha*u is:', 6 * u)
print('u*v is:', u * v)
print('unit vector u is:', LA.norm(u))

#Q3
print('A + C is not defined.')
print('A - C^T is: ', A - C.T)
print('C^T + 3D is:', C.T + 3*D)
print('B*A is:', np.dot(B, A))
print('B*A.T is not defined')

#Optional
print('B*C is not defined.')
print('C*B is:', np.dot(C, B))
print('B^4 is:', np.dot(B, np.dot(B, (np.dot(B, B)))))
print('A*A^T is:', np.dot(A, A.T))
print('D^T*D is:', np.dot(D.T, D))