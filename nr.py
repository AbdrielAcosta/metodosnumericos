'''
Created on 11 may. 2023

@author: ja_ab
'''

import random
import sympy as sp

# Genera una función aleatoria
x = sp.symbols('x')
funcion_aleatoria = 0
for i in range(5):
    coeficiente = random.randint(-10, 10)
    exponente = random.randint(1, 5)
    funcion_aleatoria += coeficiente * x**exponente

# Imprime la función aleatoria generada
print("La función aleatoria generada es: ")
sp.pprint(funcion_aleatoria)

# Resuelve el problema de Newton-Raphson
# Elegimos un punto de partida aleatorio
punto_partida = random.uniform(-10, 10)
# Definimos la derivada de la función aleatoria
derivada_funcion = sp.diff(funcion_aleatoria)
# Establecemos un límite de iteraciones
limite_iteraciones = 100
# Establecemos un umbral de convergencia
umbral_convergencia = 0.0001
# Realizamos el método de Newton-Raphson
iteracion = 1
x0 = punto_partida
while iteracion <= limite_iteraciones:
    fx = funcion_aleatoria.subs(x, x0)
    dfx = derivada_funcion.subs(x, x0)
    x1 = x0 - fx/dfx
    if abs(x1 - x0) < umbral_convergencia:
        print("El resultado de Newton-Raphson es: ", x1)
        break
    x0 = x1
    iteracion += 1
