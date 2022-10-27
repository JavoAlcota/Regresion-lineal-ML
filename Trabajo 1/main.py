from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import time

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
num_iters = 1500

def funcionCosto(t0, t1, m, X, Y):
    sum = 0
    for i in range (0, m):
        sum += (((t0 + t1 * X[i][1]) - Y[i][0]))**2
    return (1/(2*m))*sum


histCosto = []
histIter = []
histt0 = []
histt1 = []

def funcionGradiente(t0, t1, alpha, num_iters, m, X, Y):
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
        histt0.append(t0)
        histt1.append(t1)
    return temp0 , temp1, min

def graficoInicial(x, y):
    plt.scatter(x, y, color = 'red', marker='x')
    hyp = []
    yNormal = []
    for i in x:
        hyp.append(theta0 + theta1 * i)
        yNormal.append(tempp[0][0] + tempp[1][0] * i)

    plt.plot(x, hyp, label ="Gradiente descendente")
    plt.plot(x, yNormal, color = "green", label ="Ecuación normal")
    plt.title("Diagrama de dispersión de datos de entrenamiento:")
    plt.xlabel("Población de la ciudad en 10.000s")
    plt.ylabel("Beneficio en $10.000s")
    plt.legend()
    plt.show()

#dibujado punto por punto del costo vs iteraciones
def graficoCosto(frame):
    if (frame*10 >= 1500):
        anim.event_source.stop()
    else:
        tempIter.append(frame*10)
        tempCosto.append(histCosto[frame*10])
        #print(histIter[frame*10], histCosto[frame*10])
        line.set_data(tempIter, tempCosto)
        figure.gca().relim()
        figure.gca().autoscale_view()
        return line,
    
#valores the theta 0 y theta 1 usando ecuación normal
def ecuacionNormal():
    xtras = np.transpose(X)
    mult = np.dot(xtras,X)
    inversa = np.linalg.inv(mult)
    multInversa = np.dot(inversa, xtras)
    return np.dot(multInversa,Y)

#grafico en tiempo real de la recta
def graficoRectaTR():
    y = []
    newY = []
    for i in x:
        y.append(histt0[0]+histt1[0]*i)
    
    plt.ion()
    figure, ax = plt.subplots()
    line1, = ax.plot(x, y)
    plt.xlabel("Población de la ciudad en 10.000s")
    plt.ylabel("Beneficio en $10.000s")
    
    for i in range (100):
        if (i == 99):
            for j in x:
                newY.append(theta0+theta1*j)
            print("----------------------------------------------")
            print("y =",theta0,"+",theta1,"* x")
        else:
            for j in x:
                newY.append(histt0[15*i]+histt1[15*i]*j)
            print("y =",histt0[15*i],"+",histt1[15*i],"* x")
        plt.scatter(x, Y, color = 'red', marker='x')
        line1.set_xdata(x)
        line1.set_ydata(newY)
        figure.canvas.draw()
        figure.canvas.flush_events()
        newY=[]
        time.sleep(0.001)
    plt.pause(6)

def valoresFinales():
    habitantes1 = 35000  #valor de prueba 1
    habitantes2 = 70000  #valor de prueba 2
    print("----------------------------------------------------------")
    print("Valores de theta por gradiente descendente (",num_iters,"iteraciones )",":")
    print("theta0 =", theta0)
    print("theta1 =", theta1)
    print("y =",theta0,"+",theta1,"* x")
    print("Función de costo =", costo)
    print("----------------------------------------------------------")
    print("Valores de theta por ecuación normal:")
    print("theta0 =", tempp[0][0])
    print("theta1 =", tempp[1][0])
    print("y =", tempp[0][0], "+",tempp[1][0],"* x")
    print("----------------------------------------------------------")
    print("------Valores de prueba------")
    print("El beneficio para un área de",habitantes1,"es de: $",beneficio(habitantes1))
    print("El beneficio para un área de",habitantes2,"es de: $",beneficio(habitantes2),"\n")

def z(a, b, X, Y):
    m = np.size(x)
    sum = 0
    for i in range (m):
        hipotesis = a + b*X[i][1]
        sum += (Y[i][0] - hipotesis)**2
    return sum / (2*m)

def beneficio(x):
    return (theta0 + theta1 * (x/10000))*10000



temp = funcionGradiente(theta0, theta1, alfa, num_iters, size, X, Y)  #guardo los valores thetas y el costo en un vector temporal
theta0 = temp[0]
theta1 = temp[1]
costo = temp[2]

#Ecuacion normal
tempp = ecuacionNormal()

#grafico de los datos en bruto
graficoInicial(x, Y)

#grafica en tiempo real de la funcion de costo
tempIter = []
tempCosto = []
figure = plt.figure()
line, = plt.plot_date(histIter, histCosto, '-')
anim = animation.FuncAnimation(figure, graficoCosto, interval = 1)
plt.title("Función de costo vs Iteraciones")
plt.show()

#grafico de recta en tiempo real
graficoRectaTR()

#grafico 3D
plt.close()
fig = plt.figure()
ax = Axes3D(fig)
fig.add_axes(ax)
aux0 = []
aux1 = []
for i in range (1500):
    if (i*50<1500):
        aux0.append(histt0[i*50])
        aux1.append(histt1[i*50])
aux0, aux1 = np.meshgrid(aux0, aux1)
ax.set_xlabel('Theta 0')
ax.set_ylabel('Theta 1')
ax.set_zlabel('J(θ)')
ax.plot_surface(aux0, aux1, z(aux0, aux1, X, Y))
ax.scatter(histt0, histt1, histCosto, color="r")
plt.show()

#grafico de contorno
fig, ax = plt.subplots(1, 1) 
ax.scatter(histt0, histt1, color="r")
ax.contour(aux0, aux1, z(aux0, aux1, X, Y))
ax.set_xlabel('theta 0') 
ax.set_ylabel('theta1')

# #valores de theta por gradiente descendete y por ecuación normal
valoresFinales()