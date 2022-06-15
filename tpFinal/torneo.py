from gpg import Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Torneo(object):
    def __init__(self,cantidadEquipos,nombreTorneo):
        self.fechas = {}
        self.fechasTorneo = []
        self.tiempoEfectivoTorneo = []
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
        print(len(self.fechasTorneo))
        for fechas in self.fechasTorneo:    
            for tuplas in fechas.partidos:
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

                print("*************PARTIDOS***************")
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
        self.tiempoEfectivoTorneo.append(int(fecha.tiempoEfectivoFecha*(-1)))

    def obtenerEstadisticasDeFecha(self,fecha,numeroFecha):
        self.fechas.update({numeroFecha:fecha})
        self.fechasTorneo.append(fecha)
        self.tiempoEfectivoTorneo.append(int(fecha.tiempoEfectivoFecha*(-1)))
    
    def mostrarTiempoEfectivoTorneo(self):
        print("El tiempo efectivo del torneo: ",self.tiempoEfectivoTorneo)


    def exportarEstadisticas(self):
        # fechas=self.fechasTorneo
        # fechas2 = self.fechas
        # partidos = []
        # arrFecha = {}
        # n=0
        # print("fechas: ",fechas2.keys())
        # for fecha in fechas:
        #     n+=1
        #     print("fechas {0} {1}\n".format(n,fechas))

        # data = pd.DataFrame(data= np.array(fechas2.keys()))

        # #dicFechas = self.fechas
        # print(type(fechas2))
        # for fecha in fechas:
        #     arrFecha.update(fecha)
        #     for partido in fecha.partidos:
        #         print(type(partido))
        #         partidos.append(partido)

                #print(partido)
    
	
        classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
           'Data Sciece','others']
        class1_students = [45, 15, 35, 25, 30]
        print(self.tiempoEfectivoTorneo)
        #data = pd.DataFrame(classes)
        #print (data)
        datos= []
        #data.to_excel('sample_data.xlsx', sheet_name='sheet1')
        colores = ['red','green','blue','yellow','orange','black','violet','lightblue','pink']
        plt.pie(self.tiempoEfectivoTorneo)
        #plt.pie(1)
        plt.savefig("./static/tiemposPerdidos2.png") 
        plt.show() 
        return 