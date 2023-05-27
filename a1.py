import random
import numpy as np
from scipy.optimize import fsolve
def rand():
    n = random.randint(1,15)
    return n
"""
 n = 1-5 interp lineal
 n = 6-10 ec no lineales
 n = 11-15 ec lineales
 n = 16-20 medios cuadrados
 n = 21-28 ecuaciones diferenciales ordinarias
 n = 29-32 integración
"""
def filt(n):

    if n == 1:
        #interpolación lineal
        metodo = "interpolación lineal vanilla."
    elif n == 2:
        #ndelante
        metodo = "interpolación lineal por newton hacia adelante."
    elif n == 3:
        #natrás
        metodo = "interpolación lineal por newton hacia atrás."
    elif n == 4:
        #ndifdiv
        metodo = "interpolación lineal por diferencias divididas de newton."
    elif n == 5:
        #lagrange
        metodo = "interpolación lineal por lagrange."
    elif n == 6:
        # secante
        metodo = "ecuaciones no lineales por secante."
    elif n == 7:
        # newton raphson
        metodo = "ecuaciones no lineales por newton raphson."
    elif n == 8:
        # bisectriz
        metodo = "ecuaciones no lineales por bisectriz."
    elif n == 9:
        # fposicion
        metodo = "ecuaciones no lineales por falsa posición."
    elif n == 10:
        # punto fijo
        metodo = "ecuaciones no lineales por punto fijo."
    elif n == 11:
        # montante
        metodo = "ecuaciones lineales por montante."
    elif n == 12:
        # gauss seidel
        metodo = "ecuaciones lineales por gauss seidel."
    elif n == 13:
        # gauss joran
        metodo = "ecuaciones lineales por gauss jordan."
    elif n == 14:
        # eliminacion gaussiana
        metodo = "ecuaciones lineales por eliminación gaussiana."
    elif n == 15:
        # jacobi
        metodo = "ecuaciones lineales por Jacobi."
    elif n == 16:
        # cuadratica
        metodo = "medios cuadrados por cuadrática."
    elif n == 17:
        # cubica
        metodo = "medios cuadrados por cúbica."
    elif n == 18:
        # linea recta
        metodo = "medios cuadrados por línea recta."
    elif n == 19:
        # lineal con funcion
        metodo = "medios cuadrados por lineal con función."
    elif n == 20:
        # cuadratica con funcion
        metodo = "medios cuadrados por cuadrática con función."
    elif n == 21:
        # euler hacia adelante
        metodo = "ecuaciones diferenciales ordinarias euler hacia adelante."
    elif n == 22:
        # euler hacia atras
        metodo = "ecuaciones diferenciales ordinarias euler hacia atrás."
    elif n == 23:
        # euler modificado
        metodo = "ecuaciones diferenciales ordinarias euler modificado."
    elif n == 24:
        # rk 2 orden
        metodo = "ecuaciones diferenciales ordinarias RK 2 orden."
    elif n == 25:
        # rk 3 orden
        metodo = "ecuaciones diferenciales ordinarias RK 3 orden."
    elif n == 26:
        # rk 1/3 simpson
        metodo = "ecuaciones diferenciales ordinarias RK 1/3 S."
    elif n == 27:
        # rk 3/8 simpson
        metodo = "ecuaciones diferenciales ordinarias RK 3/8 S."
    elif n == 28:
        # trapezoidal
        metodo = "integración trapezoidal."
    elif n == 29:
        # 1/3 simpson
        metodo = "integración 1/3 de simpson."
    elif n == 30:
        # 3/8 simpson
        metodo = "integración 3/8 de simpson."
    elif n == 31:
        # cotes abiertas
        metodo = "integraciön cotes abiertas."
    else:
        # cotes cerradas
        metodo = "integración cotes cerradas."

    return metodo
def problema(n):
    print("Problema: ")
    if n <= 5:
        xs = np.array([1, 2, 3, 4, 5])
        ys = np.array([3, 5, 4, 6, 8])
        x_interp = np.array([1.5, 2.5, 3.5, 4.5, 4.7])
        print(f"   x    |    y   ")
        print("-----------------------------")
        for x in xs:
            print(f"  {xs[x-1]:.1f}  |  {ys[x-1]:.2f}")
        print("En el punto: %.2f de x." % x_interp[n])
    elif n <= 10:
        if n==6:
            print("x^2 - 4x + 4")
        elif n==7:
            print("2^x - 5")
        elif n==8:
            print("sin(x) - cos(x)")
        elif n==9:
            print("log(x) - 2")
        else:
            print("xsin(x) - 1")
    elif n <= 15:
        if n == 11:
            print("2x + y - z = 2, 3x - y + 2z = 13, x + 2y + 3z = 10")
        if n == 12:
            print("x + 2y - z = 4, 2x - 3y + 2z = 3, 3x - y + z = 9")
        if n == 13:
            print("3x + y - 2z = 5, 4x - y + 3z = 3, x + 3y - z = 6")
        if n == 14:
            print("2x - y + 3z = 1, x + 2y - z = 2, 3x + 4y + z = 4")
        if n == 15:
            print("x - 2y + 3z = 5, 2x + y - z = 4, 3x - y + 2z = 7")
    elif n <= 20:
        a = 0
    elif n <= 28:
        a=0
    else:
        a=0

        return problema
def resolucion(n):
    resultado = 0
    if n <= 5:
        xs = np.array([1, 2, 3, 4, 5])
        ys = np.array([3, 5, 4, 6, 8])
        x_interp = np.array([1.5, 2.5, 3.5, 4.5, 4.7])
        resultado = np.interp(x_interp[n], xs, ys)
    elif n <= 10:
        def ec(x):
            if n == 6:
                y = x**2 - 4*x + 4
            elif n == 7:
                y = 2**x - 5
            elif n == 8:
                y = np.sin(x) - np.cos(x)
            elif n == 9:
                y = np.log(x) - 2
            else:
                y = x * np.sin(x)-1
            return y

        res = fsolve(ec, 0)
        resultado = res[0]
    elif n <= 15:
        if n == 11:
            A = np.array([[2, 1, -1],
                           [3, -1, 2],
                           [1, 2, 3]])
            b = np.array([2, 13, 10])
        elif n == 12:
            A = np.array([[1, 2, -1],
                           [2, -3, 2],
                           [3, -1, 1]])
            b = np.array([4, 3, 9])
        elif n == 13:
            A = np.array([[3, 1, -2],
                           [4, -2, 3],
                           [1, 3, -1]])
            b = np.array([5, 3, 6])
        elif n == 14:
            A = np.array([[2, -1, 3],
                           [1, 2, -1],
                           [3, 4, 1]])
            b = np.array([1, 2, 4])
        else:
            A = np.array([[1, -2, 3],
                           [2, 1, -1],
                           [3, -1, 2]])
            b = np.array([5, 4, 7])
        resultado = np.linalg.solve(A,b)
    elif n <= 20:
        a=0
    elif n <= 28:
        a=0
    else:
        a=0
    return resultado