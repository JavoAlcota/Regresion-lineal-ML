from re import X
from traceback import print_tb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# lectura y guardado de datos en los arrays "x" e "y"
datos = pd.read_csv(r'data1.txt', delimiter=',', header= None) #modificar ruta del archivo si es necesario
X = []
Y = []
x = []
size = 0
for i in datos[0]:
    X.append([1,i])
    x.append(i)
    size += 1
for j in datos[1]:
    Y.append([j])

theta0 = 0
theta1 = 0
alfa = 0.01
min = 99999999
num_iters = 1500

def funcionCosto(t0, t1, m, X, Y):
    sum = 0
    for i in range (0, m):
        sum += (((t0 + t1 * X[i][1]) - Y[i][0]))**2
    return (1/(2*m))*sum


histCosto = []
histIter = []

def funcionGradiente(t0, t1, alpha, num_iters, m, X, Y):
    #t0: theta0
    #t1: theta1
    #alpha: tasa de aprendizaje
    #num_iters: numero de iteraciones
    #m: numero de elementos
    #X: matriz de características con su sesgo
    #Y: matriz de variables objeto (valores reales de los beneficios)
    #sum0 y sum1 son las sumatorias que aparecen en la ecuación de gradiente descendente.
    #Son las sumatorias para calcular theta0 y theta 1, respectivamente.
    #hyp: hipotesis
    min = 999999
    for i in range (num_iters):
        sum0 = 0
        sum1 = 0
        for j in range (0, m):
            hyp = t0 + t1 * X[j][1]
            sum0 += (hyp - Y[j][0]) * X[j][0]
            sum1 += (hyp - Y[j][0]) * X[j][1]
        t0 -= (alpha/m) * sum0
        t1 -= (alpha/m) * sum1
        
        costo = funcionCosto(t0, t1, m, X, Y) #calculo el costo llamando a la funcion correspondiente
        histCosto.append(costo)
        if (costo < min):
            min = costo
            temp0 = t0
            temp1 = t1
        histIter.append(i+1)
    return temp0 , temp1, min

def graficoConRecta(x, y, t0, t1):
    tempy = []
    for i in x:
        tempy.append(t0+t1*i)

    plt.plot(x, tempy)
    plt.scatter(x, y, color = 'red', marker='x')
    plt.title("Diagrama de dispersión de datos de entrenamiento:")
    plt.xlabel("Población de la ciudad en 10.000s")
    plt.ylabel("Beneficio en $10.000s")
    plt.show()




temp = funcionGradiente(theta0, theta1, alfa, num_iters, size, X, Y)  #guardo los valores thetas y el costo en un vector temporal
theta0 = temp[0]
theta1 = temp[1]
costo = temp[2]


tempIter = []
tempCosto = []
def graficoCosto(frame):
    if (frame*4 >= 1500):
        animacion.event_source.stop()
    else:
        tempIter.append(frame*4)
        tempCosto.append(histCosto[frame*4])
        print(histIter[frame*4], histCosto[frame*4])
        line.set_data(tempIter, tempCosto)
        plt.xlabel("Iteraciones")
        plt.ylabel("Funcion de costo")
        figure.gca().relim()
        figure.gca().autoscale_view()
        return line,



#grafica final con thetas definitivos
graficoConRecta(x, Y, theta0, theta1)


#grafica en tiempo real de la funcion de costo
figure = plt.figure()
line, = plt.plot_date(histIter, histCosto, '-')
animacion = animation.FuncAnimation(figure, graficoCosto, interval = 1)
plt.title("Función de costo vs Iteraciones")
plt.show()


print("theta0 =", "{0:.4f}".format(theta0))
print("theta1 =", "{0:.4f}".format(theta1))
print("Función de costo =", "{0:.4f}".format(costo))