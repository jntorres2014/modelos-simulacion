import numpy as np
import matplotlib.pyplot as plt

muestra = np.random.rand(1000)
#plt.hist(muestra,color= "green")
################## B ####################
#Uniforme, con parámetros: Min: 0, Max: 1.
media= 0
desvio = 1
datos=  np.random.normal(media, desvio, 1000) 
plt.hist(datos, 20, color="yellow")
plt.show()


datosExponecial =  np.
datos.exponential(scale=beta, size=1000) 