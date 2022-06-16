from random import random, sample
import random
from matplotlib.pyplot import pink
import numpy as np
from estadio import Estadio
from partido import Partido
from torneo import Torneo
from fechas import Fechas

#cantidadEquipos = 2
#contFechas= 0
tiempoTotalPartido = 5400
#contPartido = 0
class Simulacions(object):
    def __init__(self,torneo):
        self.torneo = torneo

    def simular(self):
        cantidadEquipos = 10
        contFechas = 1
        tiempoTotalPartido = 5400
        contPartido = 1
        torneo = Torneo(cantidadEquipos=cantidadEquipos,nombreTorneo="Fernando CUP")
        cantidadPartidos, cantidadFechas = torneo.obtenerCantidadPartidos() 
        while contFechas <= cantidadFechas:
            contPartido = 1
            #print("Fechas:", contFechas)
            fecha = Fechas()
            while contPartido <= cantidadPartidos:
                estadio = Estadio("Martin cup")
                partido = Partido(estadio=estadio)
                relojPartido = 0
                fel = partido.nuevaFel()
                #print("mostrando FEl: ",fel)
                #fel = partido.crearFel()
                tiemposPerdidos = 0
                
                #Empieza un partido
                while relojPartido  <= tiempoTotalPartido  :
                    evento, avanceReloj, proxEvento= partido.obtenerEvento(fel[relojPartido])
                    if not(proxEvento is None):  
                        relojPartido += int(avanceReloj)
                        fel[relojPartido] = proxEvento
                    else:
                        relojPartido += int(avanceReloj)
                    partido.contabilizarEvento(evento,avanceReloj)
                    tiemposPerdidos= tiemposPerdidos + avanceReloj
                partido.tiempoEfectivo= relojPartido - tiemposPerdidos
                print("tiempo efectivo del partido: ",partido.tiempoEfectivo)
                fecha.obtenerEstadisticasDePartido(contPartido,partido)
                #  print(fecha)
                contPartido +=1
                #print ("        *******PARTIDO {0}*******".format(contPartido-1))
                partido.estadisticasPorPartido()
                                
            #torneo.obtenerEstadisticasDePartido(contFechas, contPartido,partido)
            #torneo.obtenerEstadisticasDePartido(fecha, contPartido,partido)
            torneo.obtenerEstadisticasDeFecha(fecha,contFechas)
            fecha.mostrarEstadisticasFecha()
            #torneo.fechas.update({contFechas-1:fecha})
            #torneo.fechasTorneo.append(fecha)
            contFechas += 1
        #torneo.obtenerEstadisticasDeTorneo()
        torneo.mostrarTiempoEfectivoTorneo()
        torneo.fechas.update({contFechas-1:fecha})
        torneo.fechasTorneo.append(fecha)
        torneo.exportarEstadisticas()
        #torneo.obtenerEstadisticasDeTorneo()
        #print(torneo.fechasTorneo)
        #print(torneo.fechas)
        #print(type(fecha))

torneo= Torneo(cantidadEquipos=10,nombreTorneo="nombre")
simu=Simulacions(torneo)
simu.simular()    
#torneo.exportarEstadisticas()

