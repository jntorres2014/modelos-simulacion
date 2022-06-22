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
# import numpy as np
# rangesPorFalta= {

# 'Gol':(0.,0.6),
# 'Lesión':(0.08),
# 'Cambio':(0.09),
# 'penal':(0.70),
# 'ingresoEspectador':(0.01)
# }

# ranges = {
#     'cambio': (0., .004),
#     'gol': (.004, .0052),
#     'lesion': (.0052, .0056),
#     'lateral': (.0056, .0064),
#     'tiroDeEsquina': (.0064, .0070),
#     'falta_amonestacion_tiroLibre': (.0070, .0083),
#     #'penal': ('dependeraDeFalta'), 
#     'ingresoEspectador': (0.0083, 0.0085),
#     'ingresoAnimal': (0.0085,0.0086),
#     'nada': (.0086, 1.)
# }


# def event_in_range(num, ranges):
#     for event, rng in ranges.items():
#         if rng[0] == 0.:
#             if rng[0] <= num <= rng[1]:
#                 return event
#         elif rng[0] < num <= rng[1]:
            
#             return event
 

# #ejemplo
# numbers = np.random.uniform(0.,1.,5400)
# gol =0
# for n in numbers:
#     print("eventos: ",event_in_range(n, ranges))
#     if event_in_range(n, ranges) == 'gol':
#         gol +=1
# print("cantidad Goles: ",gol)

# Crear un nuevo libro de trabajo 
# wb = Libro_de_trabajo () # Elija la hoja activa 
# ws1 = wb.activo 
# # Cambiarle el nombre 
# ws1.title = 'mi prueba' # Escribir algunos datos 
# para columna en el rango (1,5): 
# para fila en rango (1,6): 
# letra = obtener_columna_letra(columna) 
# ws1[letra + str(fila)] = letra + str(fila) # Crear una hoja nueva 
# ws2 = wb.create_sheet(título="Ok") 
# ws2["C1"] = "OK" # Guardar archivo (si no proporciono una dirección de archivo completa, va a 
# # la misma carpeta que el script 
# wb.save('Texto.xlsx') 

# import plotly.express as px
# df = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
# fig = px.pie(df, values='pop', names='country',
#              title='Population of American continent',
#              hover_data=['lifeExp'], labels={'lifeExp':'life expectancy'})
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()
import plotly.graph_objects as go

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

#import plotly.graph_objects as go
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.write_image("static/fig1.png")
print(type(fig))
print(fig)
fig.show()