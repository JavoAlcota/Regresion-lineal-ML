from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv(r'C:/Users/panch/OneDrive/Escritorio/Trabajos/Trabajo1IA/Trabajo 1/data1.txt', delimiter=',', header= None) #modificar ruta del archivo si es necesario
x = []
y = []
for i in datos[0]:
    x.append(i)
for j in datos[1]:
    y.append(j)


# plt.scatter(x,y, color = 'red', marker='x')
# plt.title("Diagrama de dispersión de datos de entrenamiento")
# plt.xlabel("Población de la ciudad en 10.000s")
# plt.ylabel("Beneficio en $10.000s")
# plt.show()
X = []
for i in x: #Agregando el sesgo al vector x
    X.append([1,i])
Y = []
for i in y:
    Y.append([i])

theta0 = 0
theta1 = 0
alfa = 0.01
m = np.size(x)
sumatoria0 = 0
sumatoria0 = 0
for i in range (1500):
    for j in range (0, np.size(x)):
        
        sumatoria0 = sumatoria0 + (((theta0 + theta1 * X[j][1])* X[j][0] - Y[j][0])* X[j][0])
        sumatoria1 = sumatoria0 + (((theta0 + theta1 * X[j][1])* X[j][1] - Y[j][0])* X[j][1])
    theta0 = theta0 - (alfa/m) * sumatoria0
    theta1 = theta1 - (alfa/m) * sumatoria1
print("theta0 = ", theta0)
print("theta1 = ", theta1)

# sumatoria = 0
# for j in range (0, np.size(x)):
#     sumatoria = sumatoria + (((theta0 + theta1 * X[j][1]) - Y[j][0]))**2
# print(1/(2*m)*sumatoria)