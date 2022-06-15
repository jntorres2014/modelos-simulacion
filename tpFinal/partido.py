from random import choice,random
from unittest import case
from matplotlib.pyplot import eventplot
import numpy as np
from soupsieve import match

PORCENTAJE = 0.45
cantidadDeArrivoHinchas = 10
cantidadDePartidaDeHinchas = 20
tiempoTotal= 90

adicion = 0

cantidadDeCambios=0

laterales = 0.5
cambio= 0.07
lesion =0.03
penal =0.02
ingresoHincha= 0.008 
perro = 0.003
falta = 0.5
gol = 0.04

fell = []


ranges = {
    'GOL': (0.,.004),
    'CAMBIO': (.04, 0.12),
    'LESION': (.120,0.0160),
    'LATERAL': (0.190,0.210),
    #'INTERRUPCION': (0.260,0.330),
    #'falta_amonestacion_tiroLibre': (0.330 ,0.380),
    'FALTA':(0.330 ,0.340),
    #'PENAL': ('dependeraDeFalta'), 
    'EVENTOEXTERNO': (0.380, 0.388),
    'EVENTOEXTERNO': (0.388,0.391),
    'NADA': (.12, 1.)
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
# numbers = np.random.uniform(0.,1.,10)
# for n in numbers:
#     print(event_in_range(n, ranges))


class Partido(object):
    def __init__(self,estadio):
        self.estadio = estadio

        self.tiempoActual = 0
        self.tiempoEfectivo = 0
        self.tiempoTotal = 0
        self.cantidadHinchas = self.estadio.capacidadMinima
        self.eventos = {}
        self.hinchasEsperando = 0

        self.tiempoPerdidoFaltas = 0
        self.tiempoPerdidoCambios = 0
        self.tiempoPerdidoLaterales= 0
        self.tiempoPerdidoPenal = 0
        self.tiempoPerdidoGol = 0
        self.tiempoPerdidoLesionados= 0
        self.tiempoPerdidoAforo = 0
        self.tiempoPerdidoEventoExterno = 0 
        self.tiempoPerdidoNada = 0

        self.cantCambios = 0
        self.cantLaterales= 0
        self.cantPenal = 0
        self.cantGol = 0
        self.cantLesionados= 0
        self.cantAforo = 0
        self.cantEventoExterno = 0 
        self.cantFaltas = 0
        self.cantNada = 0
        #self.estadisticas= {}
        self.reloj=0
        
    def __str__(self):
        return self.estadisticasPorPartido()
        #return "Estadio: %s Capacidad: %s Capacidad Minima: %s Cantidad de Accesos: %s" % (self.nombre, self.capacidad,self.capacidadMinima, self.cantidadAcceso)

    def nuevaFell(self):
        numbers = np.random.uniform(0.,1.,6400)
        for n in numbers:
            if event_in_range(n, ranges) is None:
                fell.append('NADA')
            else:
                fell.append(event_in_range(n, ranges))
        return fell

    def event_in_range(num, ranges):
        for event, rng in ranges.items():
            if rng[0] == 0.:
                if rng[0] <= num <= rng[1]:
                    return event
            elif rng[0] < num <= rng[1]:
                return event
 
        

    def contabilizarEvento(self,evento,tiempo):
        #print("Evento: ",evento)
        if (evento=='GOL'):
            self.cantGol += 1
            self.tiempoPerdidoGol += tiempo
        if cantidadDeCambios < 6:    
            if (evento=='CAMBIO'):
                self.cantCambios +=1
                self.tiempoPerdidoCambios += tiempo
        if (evento=='LATERAL'):
            self.cantLaterales +=1  
            self.tiempoPerdidoLaterales += tiempo
        if (evento=='PENAL'):
            self.cantPenal += 1
            self.tiempoPerdidoPenal += tiempo
        if (evento=='LESION'):
            self.cantLesionados +=1
            self.tiempoPerdidoLesionados += tiempo
        if (evento=='AFORO'):
            self.cantAforo +=1
            self.tiempoPerdidoAforo += tiempo
        if (evento=='EVENTOEXTERNO'):
            self.cantEventoExterno += 1 
            self.tiempoPerdidoEventoExterno += tiempo           
        if (evento=='FALTA'):
            self.cantFaltas +=1
            self.tiempoPerdidoFaltas += tiempo
        if (evento=='NADA'):
            self.cantNada +=1
            self.tiempoPerdidoNada += tiempo


    def agregarEvento(self, tiempo,evento):
        self.eventos.update({tiempo:evento})

    def verEvento(self,evento):
        proxEvento = 'NADA'

        #print("eventos: ",evento)
        if (evento == 'GOL'):
            tiempoPerdido = np.random.uniform(45,120)
            #probabilidad de que se vayan hinchas
            probabilidad = np.random.randint(1,5)
            if probabilidad == 1:
                self.cantidadHinchas = self.cantidadHinchas - np.random.randint(10,20) #cantidadDePartidaDeHinchas
                if not(self.estadio.cumpleAforo(self.cantidadHinchas)):                
                    proxEvento = 'AFORO'        
        if (evento == 'CAMBIO'):
            if(self.cantCambios < 6):
                #self.cantCambios +=1
                tiempoPerdido = np.random.uniform(10,45)
            else:
                evento = 'NADA'
                tiempoPerdido = 0

        if (evento == 'FALTA'):
            tiempoPerdido= np.random.uniform(5,30)
            probabilidad = np.random.randint(1,50)
            if probabilidad == 1:
                proxEvento = 'LESION'
            if probabilidad == 4:
                proxEvento = 'PENAL'            
        # Probabilidad de Penales
        if (evento == 'PENAL'):
            tiempoPerdido = np.random.uniform(45,240)
            probabilidad = np.random.randint(1,2)
            if probabilidad == 1 :
                proxEvento = 'GOL'
            else: proxEvento = None      
        if (evento == 'LATERAL'):      
            tiempoPerdido = np.random.uniform(5,15)
        if (evento == 'LESION'):
            tiempoPerdido = np.random.uniform(30,120)
            proxEvento = 'CAMBIO'
        if (evento == 'AFORO'):
            tiempoPerdido = np.random.uniform(30,60)
            #proxEvento == 'ARRIVOS'
        if (evento == 'ARRIVOS'):
            #si cantidad de hichas < capacidad Estadio Meto hinchas

            if self.cantidadHinchas < self.estadio.capacidad:
                cantidadIngresantes =  np.random.randint(10,20)
                #si la cantidad de hinchas que  quiere ingresar sigue siendo menor entra
                if self.cantidadHinchas + cantidadIngresantes < self.estadio.capacidad:
                    self.cantidadHinchas += cantidadIngresantes
                #sino debo calcular la cantidad de hinchas que pueden entrar
                # y los que quedan esperando    
                else:
                    ingresantes = (self.cantidadHinchas + cantidadIngresantes)- self.estadio.capacidad
                    self.cantidadHinchas += ingresantes
                    resto = cantidadIngresantes - ingresantes
                    self.hinchasEsperando = resto
        if (evento == 'EVENTOEXTERNO'):
            tiempoPerdido = np.random.randint(60,300)
        if (evento == 'NADA'):
            tiempoPerdido = 1
            proxEvento= None
            #tiempoPerdido = np.random.uniform(5,45)
            #listaPosiblesEventos.update({'NADA':tiempoPerdido})
            #listaPosiblesEventos.append('NADA')
        #evento = choice(tuple(listaPosiblesEventos.keys()))
        
        return evento, tiempoPerdido, proxEvento

    
    
    def inicializar(self):
        self.cantidadHinchas = self.estadio.capacidadMinima
        self.eventos = self.crearFell() 
        return self.eventos           
        
    def estadisticasPorPartido(self):
        print("Estadisticas: \ntiempoFaltas: {0} \ntiempoCambios: {1} \ntiempoLaterales: {2} \ntiempoPenal: {3} \ntiempoGol: {4} \ntiempoLesionados: {5}\ntiempoAforo: {6}\ntiempoEventosExternos: {7}\n"
        .format(self.tiempoPerdidoFaltas,
        self.tiempoPerdidoCambios,
        self.tiempoPerdidoLaterales,
        self.tiempoPerdidoPenal,
        self.tiempoPerdidoGol,
        self.tiempoPerdidoLesionados,
        self.tiempoPerdidoAforo,
        self.tiempoPerdidoEventoExterno)
        )
        print("Cantidades: \ncantidad Faltas: {0}\ncantidad Cambios: {1}\ncantidad Laterales: {2} \ncantidad Penal: {3} \ncantidad Gol: {4} \ncantidad Lesionados: {5}\ncantidad Aforo: {6}\ncantidad EventosExternos: {7}\ncantidad Nada {8} \n"
        .format(self.cantFaltas,
        self.cantCambios,
        self.cantLaterales,
        self.cantPenal,
        self.cantGol,
        self.cantLesionados,
        self.cantAforo,
        self.cantEventoExterno,
        self.cantNada)
        )
        print ("Tiempo Efectivo: ", ((5400 - (self.tiempoPerdidoFaltas+self.tiempoPerdidoCambios +self.tiempoPerdidoLaterales +self.tiempoPerdidoPenal +self.tiempoPerdidoGol+
        self.tiempoPerdidoLesionados+self.tiempoPerdidoAforo + self.tiempoPerdidoEventoExterno))/60) )
        #return "hola"

    def estadisticasFinales():
        pass