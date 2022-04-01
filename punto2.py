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

################## C ####################

# Poisson, con parámetro: λ = 6. 
lamda = 6
datos =  np.random.poisson(lam=lamda, size=1000) 
plt.hist(datos, 20, color= "black")
plt.show()

################## D ####################
#Exponencial, con parámetro:  beta= 3/4  . 
beta = 3 / 4
datos = np.random.exponential(scale=beta, size=1000)
plt.hist(datos, 20, color= "grey")
plt.show()


