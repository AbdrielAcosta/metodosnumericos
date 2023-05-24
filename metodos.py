import numpy as np
import sympy as sp


def biseccion(a, b, epsilon):
    def funcion(x):
        return 10 * x ** 3 + 6 * x ** 2 + 9

    if funcion(a) * funcion(b) >= 0:
        print("El método de bisección no es aplicable en este intervalo.")
        return None

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if funcion(c) == 0:
            break
        if funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c

    return c


def gauss_seidel():
    # Generar una matriz de coeficientes aleatoria
    n = 3  # Dimensión de la matriz
    a = np.random.rand(n, n)
    print(a)

    # Convertir la matriz en una matriz diagonal dominante
    for i in range(n):
        a[i, i] += np.sum(np.abs(a[i, :])) + np.sum(np.abs(a[:, i]))

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
            x[i] = (b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
        if np.linalg.norm(np.dot(a, x) - b) < tol:
            break

    # Imprimir la solución
    print("Solución:")
    print(x)

    resp = str(input('cual es la respuesta'))
    if x == resp:
        print('La solucion es correcta')