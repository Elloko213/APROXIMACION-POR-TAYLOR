import numpy as np

# Definir la matriz y el vector
A = np.array([[0.52, 0.2, 0.25], 
              [0.3, 0.5, 0.2], 
              [0.18, 0.3, 0.55]])

b = np.array([4800, 5810, 5690])

# Método de Gauss-Seidel con un número fijo de iteraciones
def gauss_seidel_fixed_iterations(A, b, iterations=7):
    x = np.zeros_like(b)
    
    for k in range(iterations):
        x_new = np.copy(x)
        
        for i in range(A.shape[0]):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        x = x_new
    
    return x

# Resolver usando Gauss-Seidel con 7 iteraciones
solution_7_iter = gauss_seidel_fixed_iterations(A, b)
print("Solución después de 7 iteraciones:", solution_7_iter)
