import numpy as np
import sympy as sp
import random
import math
import matplotlib.pyplot as plt


# Método generar función


def generar_funcion():
    grado = random.randint(1, 3)
    coeficientes = [random.randint(-10, 10) for _ in range(grado + 1)]
    x = sp.symbols('x')
    funcion = 0
    for i in range(grado + 1):
        funcion += coeficientes[i] * x ** (grado - i)
    return funcion


# 1 Método Bisección


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


# 2 Método Gauss-Seidel


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


# 3 Método Newton Raphson


def nr():
    # Genera una función aleatoria
    x = sp.symbols('x')
    funcion_aleatoria = 0
    for i in range(5):
        coeficiente = random.randint(-10, 10)
        exponente = random.randint(1, 5)
        funcion_aleatoria += coeficiente * x ** exponente

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
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < umbral_convergencia:
            print("El resultado de Newton-Raphson es: ", x1)
            break
        x0 = x1
        iteracion += 1


# 4 Método Secante


def secante():
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


# 5 Método falsa posición


def fp():
    def f(x):
        # Aquí se define la función aleatoria
        return random.uniform(-10, 10) * x ** 2 + random.uniform(-10, 10) * x + random.uniform(-10, 10)

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


# 6 Método punto fijo


def pf():
    def f(x):
        return x * x * x + x * x - 1

    # Re-writing f(x)=0 to x = g(x)
    def g(x):
        return 1 / math.sqrt(1 + x)

    # Implementing Fixed Point Iteration Method
    def fixedPoint(x0, e, N):
        step = 1
        flag = 1
        condition = True
        while condition:
            x1 = g(x0)
            x0 = x1

            step = step + 1

            if step > N:
                flag = 0
                break

            condition = abs(f(x1)) > e

        if flag == 1:
            print('\nRaíz: %0.8f' % x1)
        else:
            print('\nNo Convergente.')


# 7 Método trapezoidal
def mtrap():
    # Define function to integrate
    def f(x):
        return 1 / (1 + x ** 2)

    # Implementing trapezoidal method
    def trapezoidal(x0, xn, n):
        # calculating step size
        h = (xn - x0) / n

        # Finding sum
        integracion = f(x0) + f(xn)

        for i in range(1, n):
            k = x0 + i * h
            integracion = integracion + 2 * f(k)

        # Finding final integration value
        integracion = integracion * h / 2

        print("%0.6f" %(integracion))


# 8 Método 1/3 de Simpson


def s13():
    def f(x):
        return 1 / (1 + x ** 2)

    # Implementing Simpson's 1/3
    def simpson13(x0, xn, n):
        # calculating step size
        h = (xn - x0) / n

        # Finding sum
        integracion = f(x0) + f(xn)

        for i in range(1, n):
            k = x0 + i * h

            if i % 2 == 0:
                integracion = integracion + 2 * f(k)
            else:
                integracion = integracion + 4 * f(k)

        # Finding final integration value
        integracion = integracion * h / 3

        print("%0.6f" % (integracion))


# 9 Método 3/8 de Simpson


def s38():
    # Simpson's 3/8 Rule

    # Define function to integrate
    def f(x):
        return 1 / (1 + x ** 2)

    # Implementing Simpson's 3/8
    def simpson38(x0, xn, n):
        # calculating step size
        h = (xn - x0) / n

        # Finding sum
        integracion = f(x0) + f(xn)

        for i in range(1, n):
            k = x0 + i * h

            if i % 3 == 0:
                integracion = integracion + 2 * f(k)
            else:
                integracion = integracion + 3 * f(k)

        # Finding final integration value
        integracion = integracion * 3 * h / 8

        # Finding final integration value
        integracion = integracion * h / 3

        print("%0.6f" % (integracion))


#jacobi 10

def jacobi(n):
    def generate_jacobi_problem(n):
    # Generar una matriz diagonal aleatoria
     diagonal = np.random.rand(n)
     A = np.diag(diagonal)

    # Generar una matriz aleatoria 
    B = np.random.rand(n, n)

    # Asegurarse de que la matriz de coeficientes sea diagonalmente dominante
    np.fill_diagonal(B, 0)  # Establecer los elementos de la diagonal en cero
    row_sums = np.sum(np.abs(B), axis=1)
    np.fill_diagonal(B, row_sums + 1)

    # Generar un vecto
    x = np.random.rand(n)

    # Calcular el vector
    b = np.dot(A, x)

    return A, B, b, x

        # definir el problema
n = 5
A, B, b, x = jacobi(n)

#lagrange 10

def lagrange():
    import numpy as np

def generate_lagrange_problem(n):
    # Generar valores aleatorios para los puntos x y las funciones f(x)
    x = np.random.rand(n)
    f = np.random.rand(n)

    # Calcular el polinomio de Lagrange
    def lagrange_polynomial(xi):
        result = 0
        for j in range(n):
            term = f[j]
            for k in range(n):
                if k != j:
                    term *= (xi - x[k]) / (x[j] - x[k])
            result += term
        return result

    # Generar una función aleatoria para evaluar
    target_x = np.random.rand()
    target_f = lagrange_polynomial(target_x)

    # Mostrar el problema generado
    print("Problema de Lagrange:")
    print("Puntos:")
    for i in range(n):
        print("x{} = {}, f{} = {}".format(i+1, x[i], i+1, f[i]))
    print("Evaluar en x = ?, f(x) = ?")
    print("x = {}".format(target_x))
    print("f(x) = ? (Valor objetivo)")

    return x, f, target_x, target_f

# Generar un problema de lagrange
x, f, target_x, target_f = generate_lagrange_problem(5)

def newtondfd(x,y):
    n = len(x)
    coefficients = np.zeros((n, n))
    coefficients[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coefficients[i][j] = (coefficients[i+1][j-1] - coefficients[i][j-1]) / (x[i+j] - x[i])

    return coefficients[0]

def newton_interpolation(x, y):
    coefficients = newtondfd(x, y)
    n = len(x)
    def polynomial(t):
        result = coefficients[-1]
        for i in range(n - 2, -1, -1):
            result = result * (t - x[i]) + coefficients[i]
        return result
    return polynomial

# Generar datos aleatorios
num_points = np.random.randint(5, 10)
x = np.sort(np.random.uniform(-10, 10, num_points))
y = np.random.uniform(-10, 10, num_points)

# Resolver el problema de interpolación
polynomial = newton_interpolation(x, y)

# Graficar los puntos y el polinomio interpolante
t = np.linspace(x[0], x[-1], 100)
plt.scatter(x, y, color='red', label='Datos')
plt.plot(t, polynomial(t), color='blue', label='Polinomio Interpolante')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación de Newton con Diferencias Divididas')
plt.grid(True)
plt.show()


#newton hacia adelante 12

def generar_datos_aleatorios(n):
    # Generar valores aleatorios para x y f(x)
    datos = []
    for _ in range(n):
        x = random.uniform(0, 1)  # Valor aleatorio para x en el rango [0, 1]
        fx = random.uniform(-100, 100)  # Valor aleatorio para f(x) en el rango [-100, 100]
        datos.append((x, fx))
    return datos

def diferenciacion_newton_adelante(datos):
    n = len(datos)
    h = datos[1][0] - datos[0][0]  # Intervalo de diferencia (espaciado uniforme)
    
    # Calcular diferencias divididas
    diferencias_divididas = [[datos[i][1] for i in range(n)]]
    for i in range(1, n):
        diferencias_divididas.append([])
        for j in range(n - i):
            diferencia = (diferencias_divididas[i - 1][j + 1] - diferencias_divididas[i - 1][j])
            diferencia /= (datos[j + i][0] - datos[j][0])
            diferencias_divididas[i].append(diferencia)
    
    # Calcular derivada aproximada
    derivada_aproximada = diferencias_divididas[0][0]
    
    return derivada_aproximada

# Generar datos aleatorios
datos_aleatorios = generar_datos_aleatorios(5)  # Cambia el número de datos si lo deseas

# Calcular la derivada aproximada
derivada_aproximada = diferenciacion_newton_adelante(datos_aleatorios)

# Imprimir resultados
print("Datos:")
for dato in datos_aleatorios:
    print(f"x = {dato[0]}, f(x) = {dato[1]}")
print("Derivada aproximada:", derivada_aproximada)

#newton atras 13

def newtonatras():
            import random

def newton_hacia_atras(valores_iniciales, n):
    # Generar valores aleatorios para la función y sus derivadas
    funcion = [random.uniform(-10, 10) for _ in range(n)]
    derivadas = [[random.uniform(-10, 10) for _ in range(n-i)] for i in range(n)]

    # Imprimir los valores generados
    print("Función:", funcion)
    print("Derivadas:")
    for i in range(n):
        print(f"  Derivada {i+1}: {derivadas[i]}")

    # Calcular los valores de Newton hacia atrás
    valores = valores_iniciales.copy()
    for i in range(n):
        suma = 0
        for j in range(i+1):
            producto = 1
            for k in range(j):
                producto *= (valores_iniciales[i] - k)
            suma += derivadas[i][j] * producto
        valores[i] = funcion[i] - suma

    # Imprimir los resultados
    print("Valores de Newton hacia atrás:")
    for i in range(n):
        print(f"  Valor {i+1}: {valores[i]}")

# Generar valores iniciales aleatorios
valores_iniciales = [random.uniform(-10, 10) for _ in range(5)]

# Definir la cantidad de pasos de Newton hacia atrás
n = 5

# Ejecutar el método de Newton hacia atrás
newton_hacia_atras(valores_iniciales, n)


import random

def f(x, y):
    """Función diferencial dy/dx"""
    return x * y

def runge_kutta(h, x0, y0, n):
    """Implementación del método de Runge-Kutta de segundo orden"""
    print(f"n\tx\ty")
    print("-"*25)

    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h, y0 + k1)
        y1 = y0 + 0.5 * (k1 + k2)
        x1 = x0 + h

        print(f"{i+1}\t{x1}\t{y1}")

        x0 = x1
        y0 = y1

# Valores aleatorios
h = random.uniform(0.1, 0.5)
x0 = random.uniform(0, 5)
y0 = random.uniform(0, 5)
n = random.randint(5, 10)

runge_kutta(h, x0, y0, n)

runge kutta segundo orden 

import numpy as np

def f(t, y):
    # Función f(t, y) del problema de valor inicial
    return t * y  # Ejemplo: dy/dt = t * y

def runge_kutta(t0, y0, h, num_steps):
    # Inicializar arrays para almacenar los resultados
    t = np.zeros(num_steps+1)
    y = np.zeros(num_steps+1)
    
    # Asignar condiciones iniciales
    t[0] = t0
    y[0] = y0
    
    # Implementar el método de Runge-Kutta
    for i in range(num_steps):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        y[i+1] = y[i] + k2
        t[i+1] = t[i] + h
    
    return t, y

# Valores aleatorios para el problema
t0 = 0  # Valor inicial de t
y0 = np.random.rand()  # Valor inicial de y (aleatorio)
h = 0.1  # Tamaño del paso
num_steps = 10  # Número de pasos

# Llamar a la función de Runge-Kutta
t, y = runge_kutta(t0, y0, h, num_steps)

# Imprimir los resultados
for i in range(num_steps+1):
    print(f"t = {t[i]}, y = {y[i]}")

runge kutta

euler modificado

import random

def euler_modificado(f, x0, y0, h, n):
    x = x0
    y = y0
    
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        y = y + k2
        x = x + h
    
    return y

# Función de prueba: dy/dx = x + y
def f(x, y):
    return x + y

# Valores iniciales
x0 = random.uniform(0, 1)
y0 = random.uniform(0, 1)

# Paso y número de iteraciones
h = random.uniform(0.01, 0.1)
n = random.randint(10, 20)

# Calcula el resultado
resultado = euler_modificado(f, x0, y0, h, n)

# Imprime los resultados
print("Valores iniciales:")
print("x0 =", x0)
print("y0 =", y0)
print("Paso y número de iteraciones:")
print("h =", h)
print("n =", n)
print("Resultado:")
print("y(x) =", resultado)

runge kutta orden superior

import random

def f(t, y):
    """Función que define la ecuación diferencial dy/dt = f(t, y)"""
    return y**2 - t

def runge_kutta(f, a, b, h, y0):
    """Implementación del método de Runge-Kutta de orden superior"""
    t_values = []
    y_values = []

    t = a
    y = y0

    while t <= b:
        t_values.append(t)
        y_values.append(y)

        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)

        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h

    return t_values, y_values

# Valores iniciales
a = 0
b = 1
h = 0.1
y0 = random.uniform(-1, 1)  # Valor inicial aleatorio entre -1 y 1

# Resolver la ecuación diferencial utilizando Runge-Kutta
t_values, y_values = runge_kutta(f, a, b, h, y0)

# Imprimir los resultados
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.4f}")
    
    

runge kutta tercer orden

import random

def f(x, y):
    return 2 * x - y

def runge_kutta_third_order(x0, y0, h, num_steps):
    print("Iteración 0: x =", x0, "y =", y0)
    for i in range(1, num_steps + 1):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h, y0 - k1 + 2*k2)
        
        y1 = y0 + (k1 + 4*k2 + k3) / 6
        x1 = x0 + h
        
        print("Iteración", i, ": x =", x1, "y =", y1)
        
        x0, y0 = x1, y1

# Valores aleatorios
x0 = random.uniform(0, 1)
y0 = random.uniform(0, 1)
h = random.uniform(0.1, 0.5)
num_steps = random.randint(5, 10)

runge_kutta_third_order(x0, y0, h, num_steps)

cuadrática cúbica

import numpy as np

def generar_problema_aleatorio():
    # Generar coeficientes aleatorios para la función cuadrática
    a = np.random.randint(-10, 10)
    b = np.random.randint(-10, 10)
    c = np.random.randint(-10, 10)

    # Generar valor inicial aleatorio para la raíz
    x0 = np.random.randint(-10, 10)

    return a, b, c, x0

def cuadratica_cubica(a, b, c, x0, tolerancia=1e-6, max_iter=100):
    x = x0
    iteracion = 0

    while iteracion < max_iter:
        f = a * x**2 + b * x + c
        fp = 2 * a * x + b
        fpp = 2 * a

        # Actualizar la raíz utilizando el método de cuadrática cúbica
        x = x - (f * fp) / (fp**2 - f * fpp)

        # Comprobar si se ha alcanzado la tolerancia
        if abs(f) < tolerancia:
            break

        iteracion += 1

    return x

# Generar un problema aleatorio
a, b, c, x0 = generar_problema_aleatorio()

# Resolver el problema utilizando cuadrática cúbica
raiz = cuadratica_cubica(a, b, c, x0)

# Imprimir los resultados
print("Coeficientes de la función cuadrática:")
print(f"a = {a}, b = {b}, c = {c}")
print("Valor inicial para la raíz: x0 =", x0)
print("Raíz encontrada:", raiz)


import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios para la línea recta
m_true = np.random.uniform(-10, 10)  # Pendiente aleatoria
b_true = np.random.uniform(-50, 50)  # Intercepto aleatorio

# Generar datos aleatorios para el problema numérico
x = np.random.uniform(-100, 100, 100)  # Valores de x aleatorios
noise = np.random.normal(0, 20, 100)  # Ruido aleatorio
y = m_true * x + b_true + noise  # Valores de y generados por la línea recta con ruido

# Resolver el problema utilizando una línea recta
m = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)  # Pendiente estimada
b = np.mean(y) - m * np.mean(x)  # Intercepto estimado

# Graficar los datos y la línea recta estimada
plt.scatter(x, y, label='Datos')
plt.plot(x, m * x + b, color='red', label='Línea Recta Estimada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Problema de Métodos Numéricos Resuelto por Línea Recta')
plt.show()



