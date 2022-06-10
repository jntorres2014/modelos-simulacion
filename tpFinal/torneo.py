import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Torneo(object):
    def __init__(self,cantidadEquipos,nombreTorneo):
        self.fechas = {}
        self.fechasTorneo = []
        self.tiempoEfectivoTorneo = 0
        self.cantidaEquipos = cantidadEquipos
        self.nombreTorneo = nombreTorneo
        self.cantidadPartidos = 0

    def obtenerEstadisticasDeTorneo(self):
        print("*************ESTADISTICAS DE TORNEO********")
        totalTiempoPerdidoFaltas = 0
        totalTiempoPerdidoCambios =0
        totalTiempoPerdidoLaterales =0
        totalTiempoPerdidoPenal=0
        totalTiempoPerdidoGol=0 
        totalTiempoPerdidoLesionados=0 
        totalTiempoPerdidoAforo=0 
        totalTiempoPerdidoEventoExterno=0  
        totalTiempoPerdidoNada=0 
        totalCantCambios=0 
        totalCantLaterales=0 
        totalCantPenal=0 
        totalCantGol=0 
        totalCantLesionados=0 
        totalCantAforo=0 
        totalCantEventoExterno=0  
        totalCantFaltas=0 
        totalCantNada=0   
        totalTiemposEfectivos= 0     
        for fecha, tuplas in self.fechas.items():
            #print(fecha)
            totalTiempoPerdidoFaltas += tuplas.tiempoPerdidoFaltas
            totalTiempoPerdidoCambios +=tuplas.tiempoPerdidoCambios
            totalTiempoPerdidoLaterales +=tuplas.tiempoPerdidoLaterales
            totalTiempoPerdidoPenal+=tuplas.tiempoPerdidoPenal
            totalTiempoPerdidoGol+=tuplas.tiempoPerdidoGol 
            totalTiempoPerdidoLesionados+=tuplas.tiempoPerdidoLesionados 
            totalTiempoPerdidoAforo+=tuplas.tiempoPerdidoAforo 
            totalTiempoPerdidoEventoExterno+=tuplas.tiempoPerdidoEventoExterno  
            totalTiempoPerdidoNada+=tuplas.tiempoPerdidoNada 
            totalCantCambios+=tuplas.cantCambios 
            totalCantLaterales+=tuplas.cantLaterales 
            totalCantPenal+=tuplas.cantPenal 
            totalCantGol+=tuplas.cantGol 
            totalCantLesionados+=tuplas.cantLesionados 
            totalCantAforo+=tuplas.cantAforo 
            totalCantEventoExterno+=tuplas.cantEventoExterno  
            totalCantFaltas+=tuplas.cantFaltas 
            totalCantNada+=tuplas.cantNada
            totalTiemposEfectivos += tuplas.tiempoEfectivo
        # totalTiempoPerdidoFaltas = totalTiempoPerdidoFaltas / 18
        # totalTiempoPerdidoCambios = totalTiempoPerdidoCambios /18
        # totalTiempoPerdidoLaterales = totalTiempoPerdidoLaterales/18
        # totalTiempoPerdidoPenal=totalTiempoPerdidoPenal /18
        # totalTiempoPerdidoGol=  totalTiempoPerdidoGol/18
        # totalTiempoPerdidoLesionados= totalTiempoPerdidoLesionados/18
        # totalTiempoPerdidoAforo= totalTiempoPerdidoAforo/18
        # totalTiempoPerdidoEventoExterno= totalTiempoPerdidoEventoExterno/18  
        # totalTiempoPerdidoNada= totalTiempoPerdidoNada/18
    
        totalTiempoPerdidoFaltas = totalTiempoPerdidoFaltas / self.cantidadPartidos
        totalTiempoPerdidoCambios = totalTiempoPerdidoCambios /self.cantidadPartidos
        totalTiempoPerdidoLaterales = totalTiempoPerdidoLaterales/self.cantidadPartidos
        totalTiempoPerdidoPenal=totalTiempoPerdidoPenal /self.cantidadPartidos
        totalTiempoPerdidoGol=  totalTiempoPerdidoGol/self.cantidadPartidos
        totalTiempoPerdidoLesionados= totalTiempoPerdidoLesionados/self.cantidadPartidos
        totalTiempoPerdidoAforo= totalTiempoPerdidoAforo/self.cantidadPartidos
        totalTiempoPerdidoEventoExterno= totalTiempoPerdidoEventoExterno/self.cantidadPartidos  
        totalTiempoPerdidoNada= totalTiempoPerdidoNada/self.cantidadPartidos

        totalCantCambios=  totalCantCambios/self.cantidadPartidos
        totalCantLaterales=  totalCantLaterales/self.cantidadPartidos
        totalCantPenal=  totalCantPenal/self.cantidadPartidos
        totalCantGol=totalCantGol /self.cantidadPartidos
        totalCantLesionados= totalCantLesionados/self.cantidadPartidos
        totalCantAforo=  totalCantAforo/self.cantidadPartidos
        totalCantEventoExterno=  totalCantEventoExterno /self.cantidadPartidos
        totalCantFaltas= totalCantFaltas /self.cantidadPartidos
        totalCantNada= totalCantNada /self.cantidadPartidos
        totalTiemposEfectivos =  totalTiemposEfectivos/self.cantidadPartidos
        print ("cantidad de partidos: ",self.cantidadPartidos)
        print("CANTIDADES")
        print(("Faltas: {0}\nCambios: {1}\nLaterales: {2}\nPenales: {3}\nGOL: {4}\nLESION: {5}\nAFORO: {6}\nEVENTO EXTERNO: {7}\nNADA: {8}\n".format(
        totalCantFaltas, 
        totalCantCambios, 
        totalCantLaterales, 
        totalCantPenal, 
        totalCantGol, 
        totalCantLesionados, 
        totalCantAforo,
        totalCantEventoExterno,  
        totalCantNada,   
        )))
        print("TIEMPOS PERDIDOS")
        print("Faltas: {0}\nCambios: {1}\nLaterales: {2}\nPenales: {3}\nGOL: {4}\nLESION: {5}\nAFORO: {6}\nEVENTO EXTERNO: {7}\nNADA: {8}\nTotal TiemposEfectivos: {9}".format(
        totalTiempoPerdidoFaltas,
        totalTiempoPerdidoCambios,
        totalTiempoPerdidoLaterales,
        totalTiempoPerdidoPenal,
        totalTiempoPerdidoGol, 
        totalTiempoPerdidoLesionados, 
        totalTiempoPerdidoAforo, 
        totalTiempoPerdidoEventoExterno,  
        totalTiempoPerdidoNada,
        totalTiemposEfectivos))

    def obtenerCantidadPartidos(self):
        cantidadFechas = (self.cantidaEquipos *2) -2
        cantidadPartidoFechas= int(self.cantidaEquipos/2)
        #cantidadPartidoTorneo = cantidadFechas * cantidadPartidoFechas
        self.cantidadPartidos = cantidadPartidoFechas
        return cantidadPartidoFechas, cantidadFechas

    def obtenerEstadisticasDePartido(self,fecha,numeroPartido,partido):
        self.fechas.update({fecha: partido}) 
        self.fechasTorneo.append(fecha)
        #print("tiempo Efectivo Fecha: ",(type(fecha)))
        self.tiempoEfectivoTorneo += fecha.tiempoEfectivoFecha
    
    def mostrarTiempoEfectivoTorneo(self):
        print("El tiempo efectivo del torneo: ",self.tiempoEfectivoTorneo)


    def exportarEstadisticas(self):
        fechas=self.fechasTorneo
        
        data = pd.DataFrame(fechas,index=fechas[], columns= tiempos[])
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