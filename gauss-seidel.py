'''
Created on 11 may. 2023

@author: ja_ab
'''

import numpy as np
from pip._internal.network.utils import response_chunks

# Generar una matriz de coeficientes aleatoria
n = 3  # Dimensión de la matriz
A = np.random.rand(n, n)
print(A)

# Convertir la matriz en una matriz diagonal dominante
for i in range(n):
    A[i,i] += np.sum(np.abs(A[i,:])) + np.sum(np.abs(A[:,i]))

# Generar un vector de términos independientes aleatorio
b = np.random.rand(n)

# Definir la tolerancia y el número máximo de iteraciones
tol = 1e-6
max_iter = 1000

# Inicializar el vector de solución
x = np.zeros(n)

# Realizar el método de Gauss-Seidel
for k in range(max_iter):
    for i in range(n):
        x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
    if np.linalg.norm(np.dot(A, x) - b) < tol:
        break

# Imprimir la solución
print("Solución:")
print(x)


resp = str( input('cual es la respuesta'))
if x == resp:
    print('La solucion es correcta')