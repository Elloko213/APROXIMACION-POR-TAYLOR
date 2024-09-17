import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]
        
        if np.linalg.norm(x - x_old, np.inf) < tol:
            break
            
    return x

A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

b = np.array([7.85, -19.3, 71.4])
x0 = np.zeros(len(b))

sol = gauss_seidel(A, b, x0, tol=1e-6, max_iter=100)
print(sol)
