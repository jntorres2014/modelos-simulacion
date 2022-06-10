from ctypes import cast
from math import log
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import punto4 

#Una transformación para que la variable aleatoria tenga una distribución de probabilidad Exponencial con parámetro   = 12.
################# A #################
muestra = np.random.rand(1000)
media= 0
desvio = 1
datosA=  np.random.normal(media, desvio, 1000) 
beta= 12
lamda= 1/beta
print(datosA)
j=0
for i in datosA:  
     datosA[j]= (-1)*(int(i))/lamda
     j=j+1
# datosExponecial =  np.exp(datosA)
# print(datosExponecial)
#datos = np.datosExponecial.exponential(scale=beta, size=1000)
#plt.hist(datosExponecial, 20, color="green")
#plt.show() 
################# B #################

################# C #################
#Genere otros 100 valores aleatorios siguiendo una distribución Exponencial con parámetro   = 3.
beta= 3
datosB = np.random.exponential(scale=beta, size=100)
plt.hist(datosB, 20, color="yellow")
plt.show()
################# D #################
#Genere 1000 valores aleatorios con las mismas características que en el inciso c.

beta= 3
datos = np.random.exponential(scale=beta, size=1000)
puntoD=plt.hist(datos, 20, color="red")

################# E #################
plt.show()

################## Punto 4 ############

# Obtengo la media de la muestra
mediaA = np.mean(datosA)
# El desvio estadar de la muestra
desvioA= np.std(datosA)
# La varianza de la muestra
varianzaA = np.var(datosA)

# Obtengo la media de la muestra
mediaB = np.mean(datosB)
# El desvio estadar de la muestra
desvioB= np.std(datosB)
# La varianza de la muestra
varianzaB = np.var(datosB)

print("el media de la primera muestra es ", mediaA)
print("el desvio standar de la primera muestra es ", desvioA)
print("el varianza de la segunda muestra es ", varianzaA)


print("el media de la segunda muestra es ", mediaB)
print("el desvio standar de la segunda muestra es ", desvioB)
print("el varianza de la segunda muestra es ", varianzaB)

intervalo_confianza = punto4.confidence_interval(1000,mediaA,3,0,0)
print(intervalo_confianza)
#intervalo2= punto4.mean_confidence_interval(datosA,0.95)

plt.hist(intervalo_confianza,10,color=['red','yellow'])
plt.show()

#plt.hist(intervalo2,10,color='red')
#print(intervalo2)
#Muestro grafico
#plt.show()
