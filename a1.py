import random
import numpy as np
def rand():
    n = random.randint(1,32)
    return n
"""
 n = 1-5 interp lineal
 n = 6-10 ec no lineales
 n = 11-15 ec lineales
 n = 16-20 medios cuadrados
 n = 21-28 ecuaciones diferenciales ordinarias
 n = 29-32 integración
"""
# Problemas de interpolacion
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 4, 6, 8])
x_interp = np.array([1.5, 2.5, 3.5, 4.5])

def filt(n):

    if(n == 1):
        #interpolación lineal
        metodo = "interpolación lineal vanilla."
    elif(n == 2):
        #ndelante
        metodo = "interpolación lineal por newton hacia adelante."
    elif(n == 3):
        #natrás
        metodo = "interpolación lineal por newton hacia atrás."
    elif(n == 4):
        #ndifdiv
        metodo = "interpolación lineal por diferencias divididas de newton."
    elif(n == 5):
        #lagrange
        metodo = "interpolación lineal por lagrange."
    elif(n == 6):
        # secante
        metodo = "ecuaciones no lineales por secante."
    elif(n == 7):
        # newton raphson
        metodo = "ecuaciones no lineales por newton raphson."
    elif(n == 8):
        # bisectriz
        metodo = "ecuaciones no lineales por bisectriz."
    elif(n == 9):
        # fposicion
        metodo = "ecuaciones no lineales por falsa posición."
    elif(n == 10):
        # punto fijo
        metodo = "ecuaciones no lineales por punto fijo."
    elif(n == 11):
        # montante
        metodo = "ecuaciones lineales por montante."
    elif(n == 12):
        # gauss seidel
        metodo = "ecuaciones lineales por gauss seidel."
    elif(n == 13):
        # gauss joran
        metodo = "ecuaciones lineales por gauss jordan."
    elif(n == 14):
        # eliminacion gaussiana
        metodo = "ecuaciones lineales por eliminación gaussiana."
    elif(n == 15):
        # jacobi
        metodo = "ecuaciones lineales por Jacobi."
    elif(n == 16):
        # cuadratica
        metodo = "medios cuadrados por cuadrática."
    elif (n == 17):
        # cubica
        metodo = "medios cuadrados por cúbica."
    elif (n == 18):
        # linea recta
        metodo = "medios cuadrados por línea recta."
    elif (n == 19):
        # lineal con funcion
        metodo = "medios cuadrados por lineal con función."
    elif (n == 20):
        # cuadratica con funcion
        metodo = "medios cuadrados por cuadrática con función."
    elif (n == 21):
        # euler hacia adelante
        metodo = "ecuaciones diferenciales ordinarias euler hacia adelante."
    elif (n == 22):
        # euler hacia atras
        metodo = "ecuaciones diferenciales ordinarias euler hacia atrás."
    elif (n == 23):
        # euler modificado
        metodo = "ecuaciones diferenciales ordinarias euler modificado."
    elif (n == 24):
        # rk 2 orden
        metodo = "ecuaciones diferenciales ordinarias RK 2 orden."
    elif (n == 25):
        # rk 3 orden
        metodo = "ecuaciones diferenciales ordinarias RK 3 orden."
    elif (n == 26):
        # rk 1/3 simpson
        metodo = "ecuaciones diferenciales ordinarias RK 1/3 S."
    elif (n == 27):
        # rk 3/8 simpson
        metodo = "ecuaciones diferenciales ordinarias RK 3/8 S."
    elif (n == 28):
        # trapezoidal
        metodo = "integración trapezoidal."
    elif (n == 29):
        # 1/3 simpson
        metodo = "integración 1/3 de simpson."
    elif (n == 30):
        # 3/8 simpson
        metodo = "integración 3/8 de simpson."
    elif (n == 31):
        # cotes abiertas
        metodo = "integraciön cotes abiertas."
    else:
        # cotes cerradas
        metodo = "integración cotes cerradas."

    return metodo

def filt2(n):


    if(n == 1):
        #interpolación lineal

    elif(n == 2):
        #ndelante
        metodo = "interpolación lineal por newton hacia adelante."
    elif(n == 3):
        #natrás
        metodo = "interpolación lineal por newton hacia atrás."
    elif(n == 4):
        #ndifdiv
        metodo = "interpolación lineal por diferencias divididas de newton."
    elif(n == 5):
        #lagrange
        metodo = "interpolación lineal por lagrange."
    elif(n == 6):
        # secante
        metodo = "ecuaciones no lineales por secante."
    elif(n == 7):
        # newton raphson
        metodo = "ecuaciones no lineales por newton raphson."
    elif(n == 8):
        # bisectriz
        metodo = "ecuaciones no lineales por bisectriz."
    elif(n == 9):
        # fposicion
        metodo = "ecuaciones no lineales por falsa posición."
    elif(n == 10):
        # punto fijo
        metodo = "ecuaciones no lineales por punto fijo."
    elif(n == 11):
        # montante
        metodo = "ecuaciones lineales por montante."
    elif(n == 12):
        # gauss seidel
        metodo = "ecuaciones lineales por gauss seidel."
    elif(n == 13):
        # gauss joran
        metodo = "ecuaciones lineales por gauss jordan."
    elif(n == 14):
        # eliminacion gaussiana
        metodo = "ecuaciones lineales por eliminación gaussiana."
    elif(n == 15):
        # jacobi
        metodo = "ecuaciones lineales por Jacobi."
    elif(n == 16):
        # cuadratica
        metodo = "medios cuadrados por cuadrática."
    elif (n == 17):
        # cubica
        metodo = "medios cuadrados por cúbica."
    elif (n == 18):
        # linea recta
        metodo = "medios cuadrados por línea recta."
    elif (n == 19):
        # lineal con funcion
        metodo = "medios cuadrados por lineal con función."
    elif (n == 20):
        # cuadratica con funcion
        metodo = "medios cuadrados por cuadrática con función."
    elif (n == 21):
        # euler hacia adelante
        metodo = "ecuaciones diferenciales ordinarias euler hacia adelante."
    elif (n == 22):
        # euler hacia atras
        metodo = "ecuaciones diferenciales ordinarias euler hacia atrás."
    elif (n == 23):
        # euler modificado
        metodo = "ecuaciones diferenciales ordinarias euler modificado."
    elif (n == 24):
        # rk 2 orden
        metodo = "ecuaciones diferenciales ordinarias RK 2 orden."
    elif (n == 25):
        # rk 3 orden
        metodo = "ecuaciones diferenciales ordinarias RK 3 orden."
    elif (n == 26):
        # rk 1/3 simpson
        metodo = "ecuaciones diferenciales ordinarias RK 1/3 S."
    elif (n == 27):
        # rk 3/8 simpson
        metodo = "ecuaciones diferenciales ordinarias RK 3/8 S."
    elif (n == 28):
        # trapezoidal
        metodo = "integración trapezoidal."
    elif (n == 29):
        # 1/3 simpson
        metodo = "integración 1/3 de simpson."
    elif (n == 30):
        # 3/8 simpson
        metodo = "integración 3/8 de simpson."
    elif (n == 31):
        # cotes abiertas
        metodo = "integraciön cotes abiertas."
    else:
        # cotes cerradas
        metodo = "integración cotes cerradas."

    return metodo

def problema(n):
    if (n <= 5):
        xs = np.array([1, 2, 3, 4, 5, 6])
        ys = np.array([3, 5, 4, 6, 8, 10])
        x_interp = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
        print("Problema:")
        print(f"   x    |    y   ")
        print("-----------------------------")
        for x in xs:
            print(f"  {x:.1f}  |  {y:.2f}")
        print("En el punto: %.2 de x." % x_interp[n])
    elif (n <= 10):

        elif (n <= 15):

        elif (n <= 20):

        elif (n <= 28):

        else:
def resolucion(n):
    if(n <= 5):
        xs = np.array([1, 2, 3, 4, 5, 6])
        ys = np.array([3, 5, 4, 6, 8, 10])
        x_interp = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
        print("Problema:")
        print(f"   x    |    y   ")
        print("-----------------------------")
        for x in xs:
            print(f"  {x:.1f}  |  {y:.2f}")
        print("En el punto: %.2 de x." % x_interp[n])
        resultado = np.interp(x_interp[n], xs, ys)
        return resultado
    elif(n <= 10):

    elif(n <= 15):

    elif(n <= 20):

    elif(n <= 28):

    else:

