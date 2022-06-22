from random import random, sample
import random
import numpy as np
from estadio import Estadio
from partido import Partido
from torneo import Torneo
from fechas import Fechas

from tpFinal import inicializador

listaDeUsuario= ['GOL','REANUDACION']
# Se puede cambiar
class Simulacion(object):
    def __init__(self):
        self.estadisticas = {}
        self.cantidadCorridas=0
        self.contadores= {}
        self.eventosPosibles = {}
        #self.reloj

    
    def atenderEvento(self,partido,evento):
        if evento == 'INTERRUPCION':
            #interrup = interrup + 1
            print("*******INTERRUPCION**************")
            #Veo que evento puede ser
            #eventosPosibles= partido.verEvento()
            #partido.revisarTipoEvento()
            tiempoPerdido = random.randint(1, 4)
            #self.tiempoInterrupciones.update({eventosPosibles[0] : tiempoPerdido})
            partido.tiempoPerdido = tiempoPerdido + partido.tiempoPerdido
            partido.eventos[reloj+tiempoPerdido] = 'REANUDACION'
            reloj= reloj + tiempoPerdido -1
        elif evento=='REANUDACION':
            reanudacion =+1
            print("**********REANUDACION***********")
            reloj= reloj +1
        elif evento=='ARRIVOS':
            arrivos +=1
            print("**********ARRIVOS***********")
            if partido.cantidadHinchas <= partido.estadio.capacidad:
                partido.cantidadHinchas += cantidadDeArrivoHinchas
                #print('Entraron Hinchas, ahora son: %i de %i ',partido.cantidadHinchas,partido.estadio.capacidad)
            else:
            #print("me quedan %s hinchas de %s",partido.cantidadHinchas,partido.estadio.capacidad)
            #Crear un evento de Interrupcion para esperar que se complete el aforo
                pass
        elif evento == 'FNC': #FALTAS NO    COBRADAS
            fnc =+1
            print("**********FALTA NO COBRADA***********")
        if random.randint(0,3) == 3:
            partido.cantidadHinchas = partido.cantidadHinchas - cantidadDePartidaDeHinchas
            #print("se fueron hinchas ahora quedan: ", partido.cantidadHinchas)
        if not partido.estadio.cumpleAforo(partido.cantidadHinchas):
            pass
        #partido.crearEventos(reloj,'NOCUMPLEAFORO')
        #crear un evento de interrucion por arrivo de hinchas.
        #print(reloj)

        pass
        
    def simular(self,cantidadCorridas,aforo,eventosPosibles):
        pass

    def simular(self):
        tiempoInterrupciones = {}
        tiempoTotal= 5400 # 90 minutos en segundos
        adicion=0
        cantidadDeArrivoHinchas=15
        cantidadDePartidaDeHinchas = 30
        simulacion = Simulacion()
        CORRIDAS = 7
        corrida = 1
        tiempoEfectivo=0
        estadisticasCorridas = {}
        while corrida <= CORRIDAS:
            tiempoInterrupciones = {}
            print("                         ***********CORRIDA NUMERO {0} ".format(corrida),"*************")
            estadio = Estadio("Fernando cup")
            partido = Partido(estadio)
            reloj=0
            contadorCambios= 0
            fnc=0
            interrup=0
            reanudacion=0
            arrivos=0
            partido.eventos = partido.inicializar()
            #print(partido.eventos)
            print(partido.eventos)
            while (reloj <= tiempoTotal + adicion):
                print("reloj: ",reloj)
                evento = partido.eventos[reloj]
                print(evento)
                evento = evento[0]
                if listaDeUsuario.index("GOL")is None:
                    print("Entro hay gol")
                if evento == 'INTERRUPCION':
                    interrup = interrup + 1
                    print("*******INTERRUPCION**************")
                    eventosPosibles= partido.verEvento()
                    print("eventos posibles",eventosPosibles)
                    #partido.revisarTipoEvento()
                    tiempoPerdido = int(eventosPosibles[1])
                    #tiempoInterrupciones.update({eventosPosibles[0] : tiempoPerdido})
                    partido.tiempoPerdido = tiempoPerdido + partido.tiempoPerdido
                    
                    partido.eventos[reloj+tiempoPerdido] = ['REANUDACION']
                    reloj= reloj + tiempoPerdido -1
                elif evento=='REANUDACION':
                    print("**********REANUDACION***********")
                    reanudacion =+1
                    tiempo = random.randint(10, 40)
                    print("Tiempo: ", tiempo)
                    tiempoEfectivo = tiempoEfectivo + tiempo 
                    reloj= reloj + tiempo -1
                if listaDeUsuario.index("REANUDACION")is None:
                    print("Entro hay gol abajos")
                elif evento=='ARRIVOS':
                    arrivos +=1
                    print("**********ARRIVOS***********")
                    if partido.cantidadHinchas <= partido.estadio.capacidad:
                        partido.cantidadHinchas += cantidadDeArrivoHinchas
                        #print('Entraron Hinchas, ahora son: %i de %i ',partido.cantidadHinchas,partido.estadio.capacidad)
                    else:
                        #print("me quedan %s hinchas de %s",partido.cantidadHinchas,partido.estadio.capacidad)
                        #Crear un evento de Interrupcion para esperar que se complete el aforo
                        pass
                elif evento == 'FNC': #FALTAS NO COBRADAS
                    fnc =+1
                    print("**********FALTA NO COBRADA***********")
                    if random.randint(0,3) == 3:
                        partido.cantidadHinchas = partido.cantidadHinchas - cantidadDePartidaDeHinchas
                        #print("se fueron hinchas ahora quedan: ", partido.cantidadHinchas)
                        if not partido.estadio.cumpleAforo(partido.cantidadHinchas):
                            pass
                            #partido.crearEventos(reloj,'NOCUMPLEAFORO')
                            #crear un evento de interrucion por arrivo de hinchas.
                #print(reloj)
                reloj = reloj + 1
                tiempoInterrupciones.update({"TIEMPO PERDIDO":partido.tiempoPerdido})

                # if reloj == tiempoTotal:
                #     print("Termino el tiempo")
                #     adicion = partido.tiempoPerdido * 0.10
                #     print("se va a reanudad: ",adicion)
            print("                         **********FIN DE PARTIDOOOO***********")   
            estadisticasCorridas.update({("Corrida {0}".format(corrida)):tiempoInterrupciones})
            print("**********ESTADISTICAS***********")     
            print("tiempo Perdido del partido",corrida,partido.tiempoPerdido)
            print ("tiempo total de partido: ",reloj-1)
            corrida += 1
            print("interrup {0} arrivos {1} reanudacion {2} fnc {3}".format(interrup,arrivos,reanudacion,fnc))
            
            for key in tiempoInterrupciones:
                print ("Interrupciones por",key, ":", tiempoInterrupciones[key])
        return tiempoInterrupciones, estadisticasCorridas
            #print(tiempoInterrupciones)
        #simulacion.estadisticas.update({corrida,partido.estadisticas})