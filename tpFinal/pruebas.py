from simulacion import Simulacion 
import pandas as pd
import matplotlib.pyplot as plt

sim = Simulacion()
tiempos=sim.simular()
# print(tiempos[1])
# print(tiempos)
#print(tiempos[1])


data = pd.DataFrame(tiempos[1],index=tiempos[0].keys(), columns= tiempos[1].keys())
print("Tiempos perdidos:",tiempos[0]["TIEMPO PERDIDO"])
datos= []
for key in tiempos[1]:
    for key2 in tiempos[1][key]:
        if key2 == 'TIEMPO PERDIDO':
            datos.append(tiempos[1][key][key2])
print(datos)
# data = pd.DataFrame({col1:list1,col2:list2})

# data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)

data.to_excel('sample_data.xlsx', sheet_name='sheet1',index="algo")

#inicializador()





#df = pd.read_excel("sample_data.xlsx")
#print(df)
#tab = pd.crosstab(index=df.index,columns=df.columns)
#print(tab)
colores = ['red','green','blue','yellow','orange']
plt.pie(datos,colors=colores) 
plt.xlabel("Perdidas de tiempo")
plt.savefig("tiemposPerdidos.png")
plt.show()