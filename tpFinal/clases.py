from cgi import print_environ
from random import random, sample
import random
import numpy as np
from estadio import Estadio
from partido import Partido
from tpFinal import inicializador

# Se puede cambiar
PORCENTAJE = 0.45
cantidadDeArriboHinchas = 10
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


    #evento)(momento en el que ocurre,tiempo de retardo)
class Interrupciones(object):
    def __init__(self,probabilidad):
        self.probabilidad = probabilidad
        


class Simulacion(object):
    def __init__(self):
        self.estadisticas = {}
                
class Evento(object):
    def __init__(self):
        self.cola= []

simulacion = Simulacion()
CORRIDAS = 10
corrida = 0
while corrida <= CORRIDAS:
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
        elif evento=='ARRIBOS':
            if partido.cantidadHinchas <= partido.estadio.capacidad:
                partido.cantidadHinchas += cantidadDeArriboHinchas
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
                    #crear un evento de interrucion por arribo de hinchas.
        reloj +=1
        # if reloj == tiempoTotal:
        #     print("Termino el tiempo")
        #     adicion = partido.tiempoPerdido * 0.10
        #     print("se va a reanudad: ",adicion)
    print("tiempo Perdido",partido.tiempoPerdido)
    print ("tiempo total de partido: ",reloj-1)
    corrida += 1
simulacion.estadisticas.update({corrida,partido.estadisticas})