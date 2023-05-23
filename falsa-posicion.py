'''
Created on 11 may. 2023

@author: ja_ab
'''

import random

def f(x):
    # Aquí se define la función aleatoria
    return random.uniform(-10, 10) * x**2 + random.uniform(-10, 10) * x + random.uniform(-10, 10)

def falsa_posicion(a, b, tol):
    # Implementación del método de falsa posición
    while True:
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(fc) < tol:
            return c
        elif fa * fc < 0:
            b = c
        else:
            a = c

# Generamos dos números aleatorios en el rango [-10, 10]
a = random.uniform(-10, 10)
b = random.uniform(-10, 10)

# Nos aseguramos que f(a) y f(b) tengan signos opuestos
while f(a) * f(b) >= 0:
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)

# Definimos la tolerancia
tol = 1e-6

# Llamamos a la función falsa_posicion con los parámetros generados aleatoriamente
raiz = falsa_posicion(a, b, tol)

print(f"La raíz de la función f(x) = {f.__name__} en el intervalo [{a}, {b}] es {raiz}")