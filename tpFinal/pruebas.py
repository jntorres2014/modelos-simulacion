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
    'cambio': (0., .004),
    'gol': (.004, .0052),
    'lesion': (.0052, .0056),
    'lateral': (.0056, .0064),
    'tiroDeEsquina': (.0064, .0070),
    'falta_amonestacion_tiroLibre': (.0070, .0083),
    #'penal': ('dependeraDeFalta'), 
    'ingresoEspectador': (0.0083, 0.0085),
    'ingresoAnimal': (0.0085,0.0086),
    'nada': (.0086, 1.)
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
