'''
Created on 18 may. 2023

@author: ja_ab
'''

import sympy as sp

def funcion(x):
    return 10*x**3 + 6*x**2 + 9

def metodo_biseccion(a, b, epsilon):
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

a = -10
b = 10
epsilon = 0.0001

solucion = metodo_biseccion(a, b, epsilon)

if solucion is not None:
    print("La solución aproximada es:", solucion)
else:
    print("No se pudo encontrar una solución en el intervalo dado.")
