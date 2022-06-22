import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Torneo(object):
    def __init__(self,cantidadEquipos,nombreTorneo):
        self.fechas = {}
        self.fechasTorneo = []
        self.tiempoEfectivoTorneo = []
        self.cantidadEquipos = cantidadEquipos
        self.nombreTorneo = nombreTorneo
        self.cantidadPartidos = 0
        self.tiemposPerdidos= self.inicializar_contadores()
        self.cantidadInterrupciones = self.inicializar_contadores()
    
    def inicializar_contadores(self):
        return {
            'FALTA': 0,
            'CAMBIO': 0,
            'LATERAL': 0,
            'PENAL': 0,
            'GOL': 0,
            'LESION': 0,
            'AFORO': 0,
            'AFORO': 0,
            'EVENTOEXTERNO': 0,
            'TIRO_DE_ESQUINA': 0,
            'NADA': 0
        }            


    def obtenerCantidadPartidos(self):
        cantidadFechas = (self.cantidadEquipos *2) -2
        cantidadPartidoFechas= int(self.cantidadEquipos/2)
        #cantidadPartidoTorneo = cantidadFechas * cantidadPartidoFechas
        self.cantidadPartidos = cantidadPartidoFechas
        return cantidadPartidoFechas, cantidadFechas

    def obtenerEstadisticasDePartido(self,fecha,numeroPartido,partido):
        self.fechas.update({fecha: partido}) 
        self.fechasTorneo.append(fecha)
        self.tiempoEfectivoTorneo.append(int(fecha.tiempoEfectivoFecha*(-1)))

    def obtenerEstadisticasDeFecha(self,fecha,numeroFecha):
        self.fechas.update({numeroFecha:fecha})
        self.fechasTorneo.append(fecha)
        self.tiempoEfectivoTorneo.append(int(fecha.tiempoEfectivoFecha*(-1)))
        print("fecha: ",fecha,"tipo", type(fecha))
        for eventos,tiempos in fecha.tiemposPerdidos.items():
                self.tiemposPerdidos[eventos] += tiempos
        for eventos,tiempos in fecha.cantidadInterrupciones.items():
            self.cantidadInterrupciones[eventos] += tiempos
        
    
    def mostrarEstadisticasDeTorneo(self):
        print("************TORNEO********")
        print("El tiempo efectivo del torneo: ",self.tiempoEfectivoTorneo)
        print("Torneo",self.cantidadInterrupciones, self.tiemposPerdidos)
