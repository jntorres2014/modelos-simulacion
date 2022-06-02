from ast import While
from dataclasses import InitVar
from mimetypes import init
import pstats
from random import random, sample
import random
import numpy as np

from tpFinal import inicializador

# Se puede cambiar
PORCENTAJE = 0.45

'''
# Usar flask para interface grafica
# Formulario para carga de datos rutas, etc.
#
'''

class Estadio(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.capacidad= random.randint(300,1000)
        self.capacidadMinima = int(self.capacidad * PORCENTAJE)
        self.cantidadAcceso= random.randint(1,3)
    
    def cumpleAforo(self, cantidadHinchas):
        return (self.capacidadMinima <= cantidadHinchas)

      

    def __str__(self):
        return "Estadio: %s Capacidad: %s Capacidad Minima: %s Cantidad de Accesos: %s" % (self.nombre, self.capacidad,self.capacidadMinima, self.cantidadAcceso)
    
    #evento)(momento en el que ocurre,tiempo de retardo)
class Interrupciones(object):
    def __init__(self,probabilidad):
        self.probabilidad = probabilidad
        
        
class Partido(object):
    def __init__(self,estadio):
        self.estadio = estadio
        self.tiempoActual = 0
        self.tiempoEfectivo = 0
        self.tiempoTotal = 0
        self.cantidadHinchas = 0
        self.eventos = {}
        
        #self.estado = ("detenido"|"enJuego")
    def agregarEvento(self, tiempo,evento):
        self.eventos.update({tiempo:evento})


    def crearEventos(self):
        eventosPosibles= ['GOL', 
        'CAMBIOS', 
        'FALTA',
        'LATERAL',
        'ARRIBO',
        'PARTIDA'
        '',]
        eventos = {}
        cont = 0
        while cont < 90:
            eventos.update({cont:(sample(eventosPosibles,k=1),np.random.uniform(45,240))})
            cont+=1        
        return eventos
    
    
    def inicializar(self):
        self.cantidadHinchas = self.estadio.capacidadMinima
        self.eventos = self.crearEventos() 
        return self.eventos           
    
        # retirandoGente = np.random.uniform(0.0,1.0)

        # cont = 0 #reloj
        # tiempoPerdido = 0
        # cantGoles = 0
        # cantFaltas = 0
        # cantCambios = 0
        # cantPenal = 0
        # cantLesion = 0
        # cantIngresoHincha = 0
        # cantLaterales = 0
        # laterales = 0.2
        # cambio= 0.07
        # lesion =0.03
        # penal =0.02
        # ingresoHincha= 0.008 
        # perro = 0.003
        # falta = 0.2
        # gol = 0.04
    
    def estadisticasPorPartido(self):
        pass
    def estadisticasFinales():
        pass

class Simulacion(object):
    def __init__(self):
        self.estadisticas = {}

    
        #Crear torneo (Cantidad de equipos)
        
        #partido (fel(relojGeneral, RelojPartido )
        #RelojGeneral()


                
class Evento(object):
    def __init__(self):
        self.cola= []
        

estadio = Estadio("Fernando cup")
partido = Partido(estadio)
print(estadio)
reloj=0
contadorCambios= 0
partido.eventos = partido.inicializar()
print(partido.eventos)


while (reloj < 90):
    evento = partido.revisarEventos(reloj,partido.eventos) 
    retardoPorHinchas = partido.revisarHinchas(evento) #
    
    # si es evento de penal, deberia crear un nuevo evento a los 2 minutos
    # si el porcentaje de gol por penal me da gol
    
    if evento == 'PENAL':
        gol = random.randint(0,1)
        if gol == 0: #hay gol
            partido.agregarEvento(reloj+2,'GOL')
            #creo el evento de gol 2 minutos mas tardes
    if evento == 'PARTIDA':
        if not (estadio.cumpleAforo(partido.cantidadHinchas)):
            #Crear evento de hincha por retardo
            partido.agregarEvento(reloj+1,'HINCHA')
    
    if evento == 'CAMBIO':
        contadorCambios += 1
    
    if evento == 'FALTA':
        penal = random.randint(0,5) #Aca intento medir la probabilidad que hay si una falta es penal
        #no se si corresponde porque tenemos un evento de penal, pero podria pasar
        if penal == 3:
            pass
            
        partido.agregarEvento()

    
    
    # reloj = reloj + 1 