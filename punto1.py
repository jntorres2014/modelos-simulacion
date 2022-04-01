import numpy as np
import matplotlib.pyplot as plt

#Creo la muestra de 100 numeros al azar 
muestra = np.random.rand(100)
#plt.hist(muestra,color= "green")

# Obtengo la media de la muestra
media = np.mean(muestra)
# El desvio estadar de la muestra
desvio= np.std(muestra)
# La varianza de la muestra
varianza = np.var(muestra)

plt.hist(muestra,10,color="red")
#Muestro grafico
plt.show()
print("muestra ",muestra)
print("La media es",media)
print("La varianza es ",varianza)
print("El desvio estandar es ", desvio)
