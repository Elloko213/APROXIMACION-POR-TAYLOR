import numpy as np

# Definición de la matriz A
A = np.array([[0.52, 0.2, 0.25],
              [0.3, 0.5, 0.2],
              [0.18, 0.3, 0.55]])

# Definición del vector b
b = np.array([4800, 5810, 5690])

# Cálculo de la inversa de A
A_inv = np.linalg.inv(A)

# Mostrar la inversa de la matriz
print("Inversa de A:")
print(A_inv)

# Resolver el sistema de ecuaciones Ax = b
x = np.linalg.solve(A, b)

# Mostrar la solución del sistema
print("\nSolución del sistema (x):")
print(x)
