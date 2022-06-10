# from simulacion import Simulacion 
# import pandas as pd
# import matplotlib.pyplot as plt

# sim = Simulacion()
# tiempos=sim.simular()

# data = pd.DataFrame(tiempos[1],index=tiempos[0].keys(), columns= tiempos[1].keys())
# print("Tiempos perdidos:",tiempos[0]["TIEMPO PERDIDO"])
# datos= []
# for key in tiempos[1]:
#     for key2 in tiempos[1][key]:
#         if key2 == 'TIEMPO PERDIDO':
#             datos.append(tiempos[1][key][key2])
# print(datos)
# data.to_excel('sample_data.xlsx', sheet_name='sheet1',index="algo")

# colores = ['red','green','blue','yellow','orange','black','violet','lightblue','pink']
# plt.pie(datos,colors=colores,labels=tiempos[1].keys()) 
# plt.xlabel("Perdidas de tiempo")
# plt.savefig("tiemposPerdidos.png")
# plt.show()
import numpy as np
rangesPorFalta= {

'Gol':(0.,0.6),
'Lesión':(0.08),
'Cambio':(0.09),
'penal':(0.70),
'ingresoEspectador':(0.01)
}
ranges = {
    'gol': (0.,.04),
    'cambio': (.04, 0.12),
    'lesion': (.120,0.0160),
    'lateral': (0.160,0.260),
    'tiroDeEsquina': (0.260,0.330),
    'falta_amonestacion_tiroLibre': (0.330 ,0.380),
    #'penal': ('dependeraDeFalta'), 
    'ingresoEspectador': (0.380, 0.388),
    'ingresoAnimal': (0.388,0.391),
    'nada': (.12, 1.)
}


def event_in_range(num, ranges):
    for event, rng in ranges.items():
        if rng[0] == 0.:
            if rng[0] <= num <= rng[1]:
                return event
        elif rng[0] < num <= rng[1]:
            
            return event
 
        
#ejemplo
numbers = np.random.uniform(0.,1.,5400)
gol =0
for n in numbers:
    print("eventos: ",event_in_range(n, ranges))
    if event_in_range(n, ranges) == 'gol':
        gol +=1
print("cantidad Goles: ",gol)
