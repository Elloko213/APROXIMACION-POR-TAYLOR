import numpy as np

# Definir la matriz de coeficientes (A) y el vector de constantes (b)
A = np.array([[0.52, 0.2, 0.25],
              [0.3, 0.5, 0.2],
              [0.18, 0.3, 0.55]])

b = np.array([4800, 5810, 5690])

# Método de Gauss-Seidel con un número específico de iteraciones
def gauss_seidel_iterations(A, b, x0=None, num_iterations=6):
    n = len(b)
    x = np.zeros_like(b) if x0 is None else x0
    for k in range(num_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        x = x_new
    return x

# Ejecutar el método con 6 iteraciones
x0 = np.zeros_like(b)
sol_6_iterations = gauss_seidel_iterations(A, b, x0, num_iterations=6)

print(sol_6_iterations)
