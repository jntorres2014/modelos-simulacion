from cgi import print_environ
from random import random, sample
import random
import numpy as np

from tpFinal import inicializador

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
        self.tiempoPerdido = 0
        
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
            listaPosiblesEventos.append('GOL')
        # Probabilidad de Cambios
        if (pCambio <= cambio)and(cantidadDeCambios < 6):
            listaPosiblesEventos.append('CAMBIO')
        # Probabilidad de Faltas cometidas
        if (pFalta <= falta):
            listaPosiblesEventos.append('FALTA')            
        # Probabilidad de Penales
        if (pPenal <= penal):
            listaPosiblesEventos.append('PENAL')            
        if (pLaterales <= laterales):
            listaPosiblesEventos.append('LATERAL')
        if (pLesion <= lesion):
            listaPosiblesEventos.append('LESION')            
        if listaPosiblesEventos == []:
            listaPosiblesEventos.append('LATERAL')
        return listaPosiblesEventos

    def crearEventos(self):
        eventosPosibles= ['GOL', 
        'CAMBIOS',
        'FALTA',
        'LATERAL',
        'ARRIVO',
        'PARTIDA'
        'LESIONADO'
        'NADA',]

        eventosPosibles2 = [
            #'INTERRUPCION',
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
        while cont < 120:
            fell.update({cont:(sample(eventosPosibles2,k=1))})
            #FEL {0:LATERAL,120}
            #FEL {0:LATERAL,120,
            #     1:FALTA,100 }
            cont+=1  
        #print(fell)
        return fell
    
    
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
#print(partido.eventos)

while (reloj <= tiempoTotal + adicion):
    evento = partido.eventos[reloj]
    print(evento)
    evento = evento[0]
    if evento ==  'INTERRUPCION':
        eventosPosibles= partido.verEvento()
        print("Estas son las interrupciones posibles",eventosPosibles)
        #partido.revisarTipoEvento()

        partido.tiempoPerdido = random.randint(1,10)+ partido.tiempoPerdido
        pass
    elif evento=='REANUDACION':

        pass
    elif evento=='ARRIVOS':
        if partido.cantidadHinchas <= partido.estadio.capacidad:
            partido.cantidadHinchas += cantidadDeArrivoHinchas
            print('Entraron Hinchas, ahora son: %i de %i ',partido.cantidadHinchas,partido.estadio.capacidad)
        else:
            print("me quedan %s hinchas de %s",partido.cantidadHinchas,partido.estadio.capacidad)
            #Crear un evento de Interrupcion para esperar que se complete el aforo
            pass
    elif evento == 'FNC': #FALTAS NO COBRADAS
        if random.randint(0,3) == 3:
            partido.cantidadHinchas = partido.cantidadHinchas - cantidadDePartidaDeHinchas
            print("se fueron hinchas ahora quedan: ", partido.cantidadHinchas)
            if not partido.estadio.cumpleAforo(partido.cantidadHinchas):
                pass
                #partido.crearEventos(reloj,'NOCUMPLEAFORO')
                #crear un evento de interrucion por arrivo de hinchas.
    reloj +=1
    # if reloj == tiempoTotal:
    #     print("Termino el tiempo")
    #     adicion = partido.tiempoPerdido * 0.10
    #     print("se va a reanudad: ",adicion)
print("tiempo Perdido",partido.tiempoPerdido)
print ("tiempo total de partido: ",reloj-1)
    #partido.revisarEventos(reloj,partido.eventos) 
    #retardoPorHinchas = partido.revisarHinchas(evento) #
    
    # si es evento de penal, deberia crear un nuevo evento a los 2 minutos
    # si el porcentaje de gol por penal me da gol
    
    # if evento == 'PENAL':
    #     gol = random.randint(0,1)
    #     if gol == 0: #hay gol
    #         partido.agregarEvento(reloj+2,'GOL')
    #         #creo el evento de gol 2 minutos mas tardes
    # if evento == 'PARTIDA':
    #     if not (estadio.cumpleAforo(partido.cantidadHinchas)):
    #         #Crear evento de hincha por retardo
    #         partido.agregarEvento(reloj+1,'HINCHA')
    
    # if evento == 'CAMBIO':
    #     contadorCambios += 1
    
    # if evento == 'FALTA':
    #     penal = random.randint(0,5) #Aca intento medir la probabilidad que hay si una falta es penal
    #     #no se si corresponde porque tenemos un evento de penal, pero podria pasar
    #     if penal == 3:
    #         pass
            
    #     partido.agregarEvento()

    
    
    # reloj = reloj + 1 