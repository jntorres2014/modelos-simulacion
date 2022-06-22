from __future__ import print_function
from sqlite3 import TimestampFromTicks
from tkinter import image_names
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from estadio import Estadio
from partido import Partido
from torneo import Torneo
import plotly.graph_objects as go
import base64
import io

from fechas import Fechas

#cantidadEquipos = 2
#contFechas= 0
tiempoTotalPartido = 5400
#contPartido = 0

rutas = { # rutas para las imgs generadas
    'tiemposPerdidosTorneo': './static/tiemposPerdidosTorneo.png',
    'cantidadesTorneo': "./static/cantidadesTorneo.png"
}



class Simulacion(object):
    def __init__(self,torneo):
        self.torneo = torneo
        self.datosTorneo = {}
        self.datosSimulacion = {}

    def simular(self,listaHabilitados,cantidadEquipos,cantidadTorneos):
        #cantidadEquipos = cantidadEquipos
        contFechas = 1
        #tiempoTotalPartido = 5400
        contPartido = 1
        #torneo = Torneo(cantidadEquipos=cantidadEquipos,nombreTorneo="Fernando CUP")
        cantidadPartidos, cantidadFechas = self.torneo.obtenerCantidadPartidos() 
        #Empieza un torneo
        contTorneo = 1
        while contTorneo <= cantidadTorneos:
            while contFechas <= cantidadFechas:
                contPartido = 1
                fecha = Fechas()
                #Empieza una fecha
                while contPartido <= cantidadPartidos:
                    estadio = Estadio("Martin cup")
                    partido = Partido(estadio=estadio)
                    relojPartido = 0
                    fell = partido.nuevaFel()
                    tiemposPerdidos = 0
                    #Empieza un partido
                    while relojPartido  <= tiempoTotalPartido :
                        evento, avanceReloj,proxEvento= partido.verEvento(fell[relojPartido])
                        if evento in listaHabilitados:
                            relojPartido += int(avanceReloj)
                        else:
                            relojPartido += 1
                        if not(proxEvento is None):  
                            #relojPartido += int(avanceReloj)
                            fell[relojPartido] = proxEvento
                            tiemposPerdidos = tiemposPerdidos + (avanceReloj)                        
                        partido.contabilizarEvento(evento,int(avanceReloj),listaHabilitados)
                        #print("avance de reloj {0} tiempo perdido {1}".format(avanceReloj, tiemposPerdidos))
                    partido.tiempoEfectivo= tiempoTotalPartido - tiemposPerdidos
                    partido.obtenerEstadisticasDePartido()
                    fecha.obtenerEstadisticasDePartido(contPartido,partido)
                    contPartido +=1
                self.torneo.obtenerEstadisticasDeFecha(fecha,contFechas)
                fecha.mostrarEstadisticasFecha()
                contFechas += 1
                self.torneo.mostrarEstadisticasDeTorneo()
            tiemposPertidos, cantidades = self.mostrarEstadisticasDeSimulacion(self.torneo)
            self.datosTorneo.update({contTorneo:[tiemposPerdidos,cantidades]})
            contTorneo +=1
        self.generarGraficos(self.torneo)
        self.datosSimulacion.update({self.torneo.nombreTorneo:self.torneo})    
        return self.datosTorneo, self.datosSimulacion
    
        
    def mostrarEstadisticasDeSimulacion(self,torneo):
        
        estadisticasTiempos= []
        estadisticasCantidades = []
        tiemposLista = []
        cantidadesLista = []
        cantidadTotalDePartidos = len(torneo.fechasTorneo) * torneo.cantidadEquipos
        for eventos,tiempos in torneo.tiemposPerdidos.items():
            #if eventos != 'NADA':
                estadisticasTiempos.append(tiempos/cantidadTotalDePartidos)
                tiemposLista.append(eventos)
                #print(eventos,type(tiempos))

        for eventos,cantidad in torneo.cantidadInterrupciones.items():
            #if eventos != 'NADA':
                estadisticasCantidades.append(cantidad/cantidadTotalDePartidos)
                cantidadesLista.append(eventos)
        plt.clf() 
        #print(estadisticasTiempos)
        #print(estadisticasCantidades)
        #colores = ['red','green','blue','yellow','orange','black','violet','lightblue','pink']
        # plt.xlabel("Cantidad de interrupciones")
        # plt.pie(estadisticasCantidades,labels=cantidadesLista,shadow=True,autopct='%1.1f%%')
        # plt.title("Cantidades de interrupciones")
        # plt.legend(loc='best')
        # plt.savefig("./static/cantidades.png")
        #plt.show()
        plt.clf() 
                
        fig = go.Figure(data=[go.Pie(labels=cantidadesLista, values=estadisticasCantidades)])
        fig.write_image(rutas['cantidadesTorneo'])
        print(type(fig))
        print(fig)
        #fig.show()
        #fig.clf()                        
        fig = go.Figure(data=[go.Pie(labels=tiemposLista, values=estadisticasTiempos)])
        fig.write_image(rutas['tiemposPerdidosTorneo'])

        # plt.pie(estadisticasTiempos,labels=tiemposLista,shadow=True,autopct='%1.1f%%')
        # plt.title("Tiempos perdidos por interrupcion")
        # plt.legend(loc='best')
        # plt.savefig("./static/tiemposPerdidos.png")
        #plt.pie(estadisticasTiempos,labels=tiemposLista)
        #plt.show()  
        #plt.pie(1)
        return estadisticasCantidades, estadisticasTiempos

    def generarGraficos(self, torneo):
        tiempoEfectivoTorneo= []
        tiemposPerdidosTorneo = []
        cantidadesPerdidasTorneo= []
        tiemposPerdidosFechas = []
        cantidadesPerdidasFechas = []
        tiempoEfectivoFecha = []
        for fechas in torneo.fechasTorneo:
            tiempoEfectivoTorneo.append(fechas.tiempoEfectivoFecha)
            tiemposPerdidosTorneo.append(fechas.tiemposPerdidos.values())
            cantidadesPerdidasTorneo.append(fechas.cantidadInterrupciones.values())
            for partido in fechas.partidos:
                tiemposPerdidosFechas.append(partido.tiemposPerdidos.values())
                cantidadesPerdidasFechas.append(partido.cantidadInterrupciones.values())
                tiempoEfectivoFecha.append(partido.tiempoEfectivo)
                
        print("TORNEO:\n Tiempo efectivo {0}\n tiempos Perdidos{1}\n Cantidades Perdidas{2}\n ".format( tiempoEfectivoTorneo,tiemposPerdidosTorneo,cantidadesPerdidasTorneo))
        print('FECHAS:\nTiempo efectivo {0}\n tiempos Perdidos{1}\n Cantidades Perdidas{2}\n '.format(tiempoEfectivoFecha,tiemposPerdidosFechas,cantidadesPerdidasFechas))

    def obtenerGrafico(self,torneo):
        print("ESTTOY EN OBTENER GRAFICO")
        print(torneo)
        img = io.BytesIO()
        datos = [52.958333333333336, 84.45833333333333, 41.75, 0.0, 87.58333333333333, 24.916666666666668, 10.791666666666666, 45.791666666666664, 0.0, 0.0]
        plt.clf() 
        plt.pie(datos, autopct="%0.1f %%")
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()



# if __name__ == '__main__':
#      torneo= Torneo(cantidadEquipos=10,nombreTorneo="nombre")
#      simu=Simulacions(torneo)
#      simu.simular(['FALTA',
#         'CAMBIO',
#         'LATERAL',
#         'PENAL',
#         'GOL',
#         'LESION',
#         'AFORO',
#         'AFORO',
#         'EVENTOEXTERNO',
#         'NADA'])
#      simu.simular([])    
#     #torneo.exportarEstadisticas()


    