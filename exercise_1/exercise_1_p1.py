import numpy as np

# a)

V = np.array([1,-1,2,2])
W = np.array([2,0,1,-1])

# b)

print("V + W = ", V + W)
print("V - W = ", V - W)
print("V^TxW = ", np.outer(V.T, W))

# c)

A = np.array([[1,-1,0,1],[2,0,-1,1],[1,1,1,1],[-1,2,1,1]])

# d)

rank_A = np.linalg.matrix_rank(A)

x = np.linalg.solve(A, V)

print("x = ", x)

# e)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues = ", eigenvalues)