
from random import random, sample
import numpy as np
# Se puede cambiar

PORCENTAJE = 0.45
cantidadDeArrivoHinchas = 10
cantidadDePartidaDeHinchas = 20
tiempoTotal= 90
adicion = 0

cantidadDeCambios=0
laterales = 0.2
cambio= 0.07
lesion =0.03
penal =0.02
ingresoHincha= 0.008 
perro = 0.003
falta = 0.2
gol = 0.04


class Partido(object):
    def __init__(self,estadio):
        self.estadio = estadio
        self.tiempoActual = 0
        self.tiempoEfectivo = 0
        self.tiempoTotal = 0
        self.cantidadHinchas = 0
        self.eventos = {}
        self.tiempoPerdido = 0
        self.estadisticas= {}
        self.reloj=0
        
        #self.estado = ("detenido"|"enJuego")
    def agregarEvento(self, tiempo,evento):
        self.eventos.update({tiempo:evento})

    def verEvento (self):
        listaPosiblesEventos= []
        pgol =np.random.uniform(0.0,1.0)
        pCambio = np.random.uniform(0.0,1.0) 
        pFalta= np.random.uniform(0.0,1.0)
        pPenal = np.random.uniform(0.0,1.0)
        pLaterales = np.random.uniform(0.0,1.0)
        pLesion = np.random.uniform(0.0,1.0)

        #Probabilidad de que ocurra un gol
        if (pgol <= gol):
            np.random.uniform(10,60)
            listaPosiblesEventos.append('GOL')
        # Probabilidad de Cambios
        if (pCambio <= cambio)and(cantidadDeCambios < 6):
            tiempo = np.random.uniform(10,45)
            listaPosiblesEventos.append('CAMBIO')
        # Probabilidad de Faltas cometidas
        if (pFalta <= falta):
            tiempo = np.random.uniform(5,60)
            listaPosiblesEventos.append('FALTA')            
        # Probabilidad de Penales
        if (pPenal <= penal):
            tiempo = np.random.uniform(45,240)
            listaPosiblesEventos.append('PENAL')            
        if (pLaterales <= laterales):
            tiempo = np.random.uniform(5,45)
            listaPosiblesEventos.append('LATERAL')
        if (pLesion <= lesion):
            tiempo = np.random.uniform(60,240)
            listaPosiblesEventos.append('LESION')            
        if listaPosiblesEventos == []:
            tiempo = np.random.uniform(5,45)
            listaPosiblesEventos.append('LATERAL')
        return listaPosiblesEventos

    def crearFell(self):
        eventosPosibles= ['GOL', 
        'CAMBIOS',
        'FALTA',
        'LATERAL',
        'ARRIVO',
        'PARTIDA'
        'LESIONADO'
        'NADA',]

        eventosPosibles2 = [
            'INTERRUPCION',
            'ARRIVOS',
            'FNC' #FALTAS NO COBRADAS
        ]
        #evento con probabilidad de ocurrencia
        dicEventos = {
            'GOL': 0.5,
            'CAMBIOS':0.3, 
            'FALTA':0.8,
            'LATERAL':0.75,
            'ARRIVO':0.60,
            'PARTIDA':0.4,
            'NADA':0.90,
            'LESIONADO':0.14,  
        }

        fell = {}
        cont = 0
        print("CREANDO FELL")
        while cont < 120:
            fell.update({cont:(sample(eventosPosibles2,k=1))})
            cont+=1  
        return fell
    
    
    def inicializar(self):
        self.cantidadHinchas = self.estadio.capacidadMinima
        self.eventos = self.crearFell() 
        return self.eventos           
        
    def estadisticasPorPartido(self,partido):
        self.estadisticas= partido

    def estadisticasFinales():
        pass