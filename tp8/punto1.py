from re import A
import numpy
from scipy.stats import ttest_ind 
# import seaborn as sns
import matplotlib.pyplot as plt

 
CORRIDAS = 250
EXPERIMENTOS = 10
FABRICACION_DIARIA = 130
COSTO_MANTENIMIENTO_STOCK = 70
INVENTARIO_INICIAL = 90
UNIDAD_MINIMA = 50

class Simulacion:
    def __init__(self):
        self.unidad_minima_actual = None
        self.costos_mantenimiento = []
        self.costos_mantenimientoAnual = []
        self.turnos_extra = []
        self.costoAnualPromedio=[]
        self.inventario = INVENTARIO_INICIAL

    def inicializar(self, unidad_minima_actual):
        self.unidad_minima_actual = unidad_minima_actual
        self.costos_mantenimiento = []
        self.turnos_extra = []
        self.inventario = INVENTARIO_INICIAL
        self.costos_mantenimientos_corrida = []
    
    def calcularCostos(self,inventario):
        self.costos_mantenimiento.append(inventario * COSTO_MANTENIMIENTO_STOCK)

    def ejecutar(self):
        simulacion = Simulacion()
        cont=0
        while cont < EXPERIMENTOS:
            corridas=0
            turnos_extra=0
            while corridas < CORRIDAS:
                demandaDiaria = int(numpy.random.normal(150, 25))
                #print("demanda diaria: ",demandaDiaria)
                simulacion.inventario = simulacion.inventario + FABRICACION_DIARIA
                #print("inventario: {0} demanda diaria:{1} ".format(simulacion.inventario,demandaDiaria))
                # Decrementamos el inventario en la demanda del día
                #print("antes de resta inventario",simulacion.inventario)
                simulacion.inventario = simulacion.inventario - demandaDiaria
                #print("despues de resta inventario:",simulacion.inventario)
                if simulacion.inventario <= UNIDAD_MINIMA:
                    # Se agrega un turno más de fabricacion
                    turnos_extra += 1
                    simulacion.inventario += FABRICACION_DIARIA
                simulacion.calcularCostos(simulacion.inventario)
                #print("inventario actual: ",simulacion.inventario)
                #print("dia ({0}) - total inventario  {1}".format(corridas, simulacion.inventario))
                #print("Cantidad de turnos: ",len(simulacion.turnos_extra))
                #simulacion.costos_mantenimientos_corrida.append(simulacion.inventario * COSTO_MANTENIMIENTO_STOCK)
                corridas +=1
            #simulacion.inventario = 90
            cont +=1
            #print(simulacion.costos_mantenimiento)
            simulacion.costoAnualPromedio.append(sum(simulacion.costos_mantenimiento)/len(simulacion.costos_mantenimiento))
            
            simulacion.costos_mantenimiento= []

            simulacion.turnos_extra.append(turnos_extra)
            print("Costo anual ({2}) Promedio {0} turnos extras: {1}".format(simulacion.costoAnualPromedio,turnos_extra,cont))
        simulacion.generar_estadisticas()
        simulacion.testDeHipotesis()    
    def generar_estadisticas(self):
        self.promedio_costo_mantenimientoAnual = sum(self.costoAnualPromedio)/len(self.costoAnualPromedio)
        promedio_turnos_extra = sum(self.turnos_extra)/len(self.turnos_extra)
        print("estadisticas: promedio costo Total: {0} Turnos Extra promedio : {1}".format(self.promedio_costo_mantenimientoAnual,self.turnos_extra))
        # print("El intervalo de confianza para el promedio anual de costo de mantenimiento (Con el 99% de confiabilidad) es de: ")
        # conf_d, conf_d_izq, conf_d_der = self.mean_confidence_interval(self.costos_mantenimiento)
        # print("+ Confianza: " + str(conf_d) + " (Izq: " + str(conf_d_izq) + " - Der: " + str(conf_d_der) + ")")
        # print("Promedio de turnos extra: " + str(promedio_turnos_extra))
        # self.generar_grafico(self.turnos_extra, '', '', 'Punto1-TurnosExtra-'+str(self.unidad_minima_actual)+'UnidadesMinimas.png')

    def testDeHipotesis(self):
        #arreglo= [416900,433580,396960,407320,393780, 391027,404892,432578,389940,412657]
        arreglo= [41690,43358,39696,40732,39378,39102,40489,43257,38994,412657]

        tset, pval =ttest_ind(self.costoAnualPromedio,arreglo)
        print("valores-p",pval) 
        if pval < 0.05: # valor alfa es 0.05 o 5% 
            print("estamos rechazando la hipotesis nula") 
        else: 
            print("estamos aceptando la hipótesis nula") 


    def mean_confidence_interval(self, data, confidence=0.99):
        pass

simulacion = Simulacion()
simulacion.ejecutar()