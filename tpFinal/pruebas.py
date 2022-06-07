from simulacion import Simulacion 
import pandas as pd
import matplotlib.pyplot as plt

sim = Simulacion()
tiempos=sim.simular()

data = pd.DataFrame(tiempos[1],index=tiempos[0].keys(), columns= tiempos[1].keys())
print("Tiempos perdidos:",tiempos[0]["TIEMPO PERDIDO"])
datos= []
for key in tiempos[1]:
    for key2 in tiempos[1][key]:
        if key2 == 'TIEMPO PERDIDO':
            datos.append(tiempos[1][key][key2])
print(datos)
data.to_excel('sample_data.xlsx', sheet_name='sheet1',index="algo")

colores = ['red','green','blue','yellow','orange','black','violet','lightblue','pink']
plt.pie(datos,colors=colores,labels=tiempos[1].keys()) 
plt.xlabel("Perdidas de tiempo")
plt.savefig("tiemposPerdidos.png")
plt.show()