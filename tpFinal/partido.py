from random import choice,random
import numpy as np
from utiles import generar_fel

PORCENTAJE = 0.45
cantidadDeArriboHinchas = 10
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

fel = []

class Partido(object):
    def __init__(self,estadio):
        self.estadio = estadio

        self.tiempoActual = 0
        self.tiempoEfectivo = 0
        self.tiempoTotal = 0
        self.cantidadHinchas = self.estadio.capacidadMinima
        self.eventos = {}
        self.hinchasEsperando = 0
        self.tiemposPerdidos = self.inicializar_contadores()
        self.cantidadInterrupciones = self.inicializar_contadores()

        self.reloj=0
    
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

    # def __str__(self):
    #     #return self.estadisticasPorPartido()
    #     return ("{0} {1} {2}".format(self.tiempoEfectivo,self.reloj,self.cantNada))
    #     #return ("Estadio: {0} Capacidad: {1} Capacidad Minima: {2} Cantidad de Accesos: {3}" ).format(self.estadio.nombre, self.estadio.capacidad,self.capacidadMinima, self.cantidadAcceso)

    def nuevaFel(self):
        numeros_aleatorios = np.random.uniform(0., 1., 6400)
        return generar_fel(numeros_aleatorios)
 
    def contabilizarEvento(self, evento, tiempo):
        self.cantidadInterrupciones[evento] += 1
        self.tiemposPerdidos[evento] += tiempo

    def agregarEvento(self, tiempo, evento):
        self.eventos.update({tiempo: evento})

    def obtenerEvento(self, evento):
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
            if(0):#self.cantCambios < 6): #???? TODO: contabilizar cambios de manera correcta. Ojo con esta condición.
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
            #proxEvento == 'ARRIBOS'
        if (evento == 'ARRIBOS'):
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
        if (evento == 'TIRO_DE_ESQUINA'):
            tiempoPerdido = np.random.randint(5, 20)
        if (evento == 'NADA'):
            tiempoPerdido = 1
            proxEvento= None
            #tiempoPerdido = np.random.uniform(5,45)
            #listaPosiblesEventos.update({'NADA':tiempoPerdido})
            #listaPosiblesEventos.append('NADA')
        #evento = choice(tuple(listaPosiblesEventos.keys()))
        #self.cantidades.update({evento:catidad})
        #self.tiemposPerdidos.update({evento:tiempoPerdido})
        return evento, tiempoPerdido, proxEvento

    
    
    def inicializar(self):
        self.cantidadHinchas = self.estadio.capacidadMinima
        self.eventos = self.crearFel() 
        return self.eventos           
        
    def estadisticasPorPartido(self):
        #print("*******TIEMPOS PERDIDOS {0}\n CANTIDADESSSSS {1}\n ".format(self.tiemposPerdidos,self.cantidadInterrupciones))
        print(f"******* \nCANTIDADES: \n {self.cantidadInterrupciones}\n")
        # print("Estadisticas: \ntiempoFaltas: {0} \ntiempoCambios: {1} \ntiempoLaterales: {2} \ntiempoPenal: {3} \ntiempoGol: {4} \ntiempoLesionados: {5}\ntiempoAforo: {6}\ntiempoEventosExternos: {7}\n"
        # .format(self.tiempoPerdidoFaltas,
        # self.tiempoPerdidoCambios,
        # self.tiempoPerdidoLaterales,
        # self.tiempoPerdidoPenal,
        # self.tiempoPerdidoGol,
        # self.tiempoPerdidoLesionados,
        # self.tiempoPerdidoAforo,
        # self.tiempoPerdidoEventoExterno)
        # )
        # print("Cantidades: \ncantidad Faltas: {0}\ncantidad Cambios: {1}\ncantidad Laterales: {2} \ncantidad Penal: {3} \ncantidad Gol: {4} \ncantidad Lesionados: {5}\ncantidad Aforo: {6}\ncantidad EventosExternos: {7}\ncantidad Nada {8} \n"
        # .format(self.cantFaltas,
        # self.cantCambios,
        # self.cantLaterales,
        # self.cantPenal,
        # self.cantGol,
        # self.cantLesionados,
        # self.cantAforo,
        # self.cantEventoExterno,
        # self.cantNada)
        # )
        # print ("Tiempo Efectivo: ", ((5400 - (self.tiempoPerdidoFaltas+self.tiempoPerdidoCambios +self.tiempoPerdidoLaterales +self.tiempoPerdidoPenal +self.tiempoPerdidoGol+
        # self.tiempoPerdidoLesionados+self.tiempoPerdidoAforo + self.tiempoPerdidoEventoExterno))/60) )
        # #return "hola"

    def estadisticasFinales():
        pass