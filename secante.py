'''
Created on 18 may. 2023

@author: ja_ab
'''

import random
import sympy as sp

def generar_funcion():
    grado = random.randint(1, 3)
    coeficientes = [random.randint(-10, 10) for _ in range(grado + 1)]
    x = sp.symbols('x')
    funcion = 0
    for i in range(grado + 1):
        funcion += coeficientes[i] * x**(grado - i)
    return funcion

def metodo_secante(funcion, x0, x1, epsilon, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)
    iteraciones = 0

    while abs(f(x1)) > epsilon and iteraciones < max_iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iteraciones += 1

    if abs(f(x1)) <= epsilon:
        return x1
    else:
        return None

funcion_aleatoria = generar_funcion()
print("Función generada:", funcion_aleatoria)

x0 = 1
x1 = 2
epsilon = 0.0001
max_iter = 100

raiz = metodo_secante(funcion_aleatoria, x0, x1, epsilon, max_iter)

if raiz is not None:
    print("La raíz aproximada es:", raiz)
else:
    print("No se pudo encontrar una raíz en el intervalo dado o se alcanzó el número máximo de iteraciones.")