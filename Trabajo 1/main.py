from re import X
from traceback import print_tb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# lectura y guardado de datos en los arrays "x" e "y"
datos = pd.read_csv(r'data1.txt', delimiter=',', header= None) #modificar ruta del archivo si es necesario
x = []
y = []
for i in datos[0]:
    x.append(i)
for j in datos[1]:
    y.append(j)



X = []
for i in x: #Agregando el sesgo al vector x
    X.append([1,i])
Y = []
for i in y:
    Y.append([i])

theta0 = 0
theta1 = 0
alfa = 0.01
size = np.size(x)
min = 99999999
num_iters = 1500
def funcionCosto(t0, t1, m, X, Y):
    sum = 0
    for i in range (0, m):
        sum += (((t0 + t1 * X[i][1]) - Y[i][0]))**2
    return (1/(2*m))*sum

def funcionGradiente(t0, t1, alpha, num_iters, m, X, Y):
    for i in range (num_iters):
        sum0 = 0
        sum1 = 0
        for j in range (0, m):
            hyp = t0 + t1 * X[j][1]
            sum0 += (hyp - Y[j][0]) * X[j][0]
            sum1 += (hyp - Y[j][0]) * X[j][1]
        t0 -= (alpha/m) * sum0
        t1 -= (alpha/m) * sum1
        
        min = 999999
        costo = funcionCosto(t0, t1, m, X, Y)
        if (costo < min):
            min = costo
            temp0 = t0
            temp1 = t1
    return temp0 , temp1, costo

def graficoConRecta(x, y, t0, t1):
    tempy = []
    for i in x:
        tempy.append(t0+t1*i)
    plt.plot(x,tempy)
    plt.scatter(x,y, color = 'red', marker='x')
    plt.title("Diagrama de dispersión de datos de entrenamiento:")
    plt.xlabel("Población de la ciudad en 10.000s")
    plt.ylabel("Beneficio en $10.000s")
    plt.show()

temp = funcionGradiente(theta0, theta1, alfa, num_iters, size, X, Y)
theta0 = temp[0]
theta1 = temp[1]
costo = temp[2]

graficoConRecta(x, y, theta0, theta1)

print("theta0 =", "{0:.4f}".format(theta0))
print("theta1 =", "{0:.4f}".format(theta1))
print("Función de costo =", "{0:.4f}".format(costo))



# for i in range (1500):
#     sumatoria0 = 0
#     sumatoria1 = 0
#     for j in range (0, size):
#         hyp = theta0 + theta1 * X[j][1]
#         sumatoria0 += ((hyp - Y[j][0])* X[j][0])
#         sumatoria1 += ((hyp - Y[j][0])* X[j][1])
#     theta0 -= (alfa/m) * sumatoria0
#     theta1 -= (alfa/m) * sumatoria1

#     #funcion de costo
#     sumatoria = 0
#     for j in range (0, np.size(x)):
#         sumatoria += (((theta0 + theta1 * X[j][1]) - Y[j][0]))**2
#     funcionDeCosto = (1/(2*m))*sumatoria
#     if (funcionDeCosto < min):
#         min = funcionDeCosto
#         a = theta0
#         b = theta1
# print("Funcion de costo minimo =",min)
# print("theta0 =",a)
# print("theta1 =",b)

# yy = []
# for i in x:
#     yy.append(a+b*i)


# plt.plot(x,yy)
# plt.scatter(x,y, color = 'red', marker='x')
# plt.title("Diagrama de dispersión de datos de entrenamiento")
# plt.xlabel("Población de la ciudad en 10.000s")
# plt.ylabel("Beneficio en $10.000s")
# plt.show()