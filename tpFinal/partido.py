import numpy as np
from utiles import generar_fel

PORCENTAJE = 0.45
cantidadDeArrivoHinchas = 10
cantidadDePartidaDeHinchas = 20
tiempoTotal= 90


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
 
    def contabilizarEvento(self,evento,tiempo,listaHabilitados):
        self.cantidadInterrupciones[evento] += 1
        if evento in listaHabilitados:
            self.tiemposPerdidos[evento] += tiempo
        
    def nuevaFel(self):
        numeros_aleatorios = np.random.uniform(0., 1., 6400)
        return generar_fel(numeros_aleatorios)

    def agregarEvento(self, tiempo,evento):
        self.eventos.update({tiempo:evento})

    def verEvento(self,evento):
        proxEvento = 'NADA'
        if (evento == 'GOL'):
            tiempoPerdido = np.random.uniform(45,120)
            #probabilidad de que se vayan hinchas
            probabilidad = np.random.randint(1,5)
            if probabilidad == 1:
                self.cantidadHinchas = self.cantidadHinchas - np.random.randint(10,20) #cantidadDePartidaDeHinchas
                if not(self.estadio.cumpleAforo(self.cantidadHinchas)):                
                    proxEvento = 'AFORO'        
        if (evento == 'CAMBIO'):
            if(self.cantidadInterrupciones[evento]<6):#self.cantCambios < 6):
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
        if (evento == 'TIRO_DE_ESQUINA'):
            tiempoPerdido = np.random.randint(5, 20)
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
        if (evento == 'TIRO_DE_ESQUINA'):
            tiempoPerdido = np.random.randint(30,70)
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
        self.eventos = self.crearFell() 
        return self.eventos           
        
    def obtenerEstadisticasDePartido(self):
        print("*************PARTIDO************")
        print(" TIEMPO perdido {0}\n CANTIDADESSSSS {1}\n ".format(self.tiemposPerdidos,self.cantidadInterrupciones))
  
    def estadisticasFinales():
        pass