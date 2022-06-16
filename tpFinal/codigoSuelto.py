
    # def simular2(self):
    #     cantidadEquipos = 10
    #     contFechas = 1
    #     tiempoTotalPartido = 5400
    #     contPartido = 1
    #     torneo = Torneo(cantidadEquipos=cantidadEquipos,nombreTorneo="Fernando CUP")
    #     cantidadPartidos, cantidadFechas = torneo.obtenerCantidadPartidos() 
    #     while contFechas <= cantidadFechas:
    #         contPartido = 1
    #         print("Fechas:", contFechas)
    #         while contPartido <= cantidadPartidos:
    #             estadio = Estadio("Martin cup")
    #             partido = Partido(estadio=estadio)
    #             relojPartido = 0
    #             fell = partido.nuevaFell()
    #             #print("mostrando FEll: ",fell)
    #             #fell = partido.crearFell()
    #             while relojPartido  <= tiempoTotalPartido  :
    #                 #partido.contabilizarEvento(fell[relojPartido],0)
    #                 #print("*********EVENTO***** ",fell[relojPartido])
    #                 #if fell[relojPartido] == 'INTERRUPCION':
    #                 if fell[relojPartido]:
    #                     evento, avanceReloj,proxEvento= partido.verEvento(fell[relojPartido])
    #                     partido.contabilizarEvento(evento,avanceReloj)
    #                     relojPartido += int(avanceReloj)
    #                     fell[relojPartido] = proxEvento
    #                     #print (proxEvento)
    #                 #elif fell[relojPartido] == 'REANUDACION':
    #                 elif fell[relojPartido] == 'NADA':
    #                     avanceReloj = random.randint(15,50)
    #                     relojPartido += int(avanceReloj)                        
    #                 else:
    #                     relojPartido += 1
    #             contPartido +=1
    #             print ("        *******PARTIDO {0}*******".format(contPartido-1))
    #             partido.estadisticasPorPartido()
            
    #         torneo.obtenerEstadisticasDePartido(contPartido,partido=partido)
    #         contFechas += 1


    # def crearFell(self,eventosPosibles):
    #     fell = {}
    #      # eventosPosibles= [# 'CAMBIO',
    #     # 'FALTA',
    #     # 'LATERAL',
    #     # 'ARRIBO',
    #     # 'PARTIDA'
    #     # 'LESIONADO'
    #     # 'NADA',]
    #     cont = 0
    #     print("CREANDO FELL")
    #     while cont < 120:
    #         fell.update({cont:self.verEvento()})
    #         #fell.update({cont:(sample(eventosPosibles,k=1))})
    #         cont+=1  
    #     return fell

    # def crearFell(self):
    #     # eventosPosibles= ['GOL', 
    #     # 'CAMBIO',
    #     # 'FALTA',
    #     # 'LATERAL',
    #     # 'ARRIBO',
    #     # 'PARTIDA'
    #     # 'LESIONADO'
    #     # 'NADA',]

    #     eventosPosibles2 = [
    #         'INTERRUPCION',
    #         'ARRIBOS',
    #         'FNC' #FALTAS NO COBRADAS
    #     ]
    #     # #evento con probabilidad de ocurrencia
    #     # dicEventos = {
    #     #     'GOL': 0.5,
    #     #     'CAMBIO':0.3, 
    #     #     'FALTA':0.8,
    #     #     'LATERAL':0.75,
    #     #     'ARRIBO':0.60,
    #     #     'PARTIDA':0.4,
    #     #     'NADA':0.90,
    #     #     'LESIONADO':0.14,  
    #     # }
    #     #fell = ['REANUDACION']
    #     cont = 0
    #     print("CREANDO FELL")
    #     while cont < 5900:
    #         #fell.update({cont:self.verEvento()})
    #         fell.append(eventosPosibles2[np.random.randint(0,2)])
    #         #fell.update({cont:(sample(eventosPosibles2,k=1))})
    #         cont+=1  
    #     return fell

#

    # def verEvento2 (self,evento):
        
    #     listaPosiblesEventos= {}
    #     pgol =np.random.uniform(0.0,1.0)
    #     pCambio = np.random.uniform(0.0,1.0) 
    #     pFalta= np.random.uniform(0.0,1.0)
    #     pPenal = np.random.uniform(0.0,1.0)
    #     pLaterales = np.random.uniform(0.0,1.0)
    #     pLesion = np.random.uniform(0.0,1.0)
    #     #Probabilidad de que ocurra un gol
    #     proxEvento = 'REANUDACION'
    #     if (pgol <= gol):
    #         #self.tiempoPerdido.update({'GOL':np.random.uniform(10,60)})
    #         tiempoPerdido = np.random.uniform(45,120)
    #         probabilidad = np.random.randint(1,5)
    #         if probabilidad == 1:
    #             self.cantidadHinchas = self.cantidadHinchas - cantidadDePartidaDeHinchas
    #             if not(self.estadio.cumpleAforo(self.cantidadHinchas)):                
    #                 pass
    #                 proxEvento = 'AFORO'        
    #             else:
    #                 proxEvento = 'REANUDACION'
    #         #listaPosiblesEventos.append('GOL')
    #         evento = 'GOL'
    #         listaPosiblesEventos.update({'GOL':tiempoPerdido})
    #         # Probabilidad de Cambios
    #     if (pCambio <= cambio):
    #         if(cantidadDeCambios < 6):
    #             evento = 'CAMBIO'
    #             tiempoPerdido = np.random.uniform(10,45)
    #             #listaPosiblesEventos.update({'CAMBIO':tiempoPerdido})
    #         else:
    #             proxEvento = 'REANUDACION'

    #         #listaPosiblesEventos.append('CAMBIO')
    #     # Probabilidad de Faltas cometidas
    #     if (pFalta <= falta):
    #         evento = 'FALTA'
    #         tiempoPerdido= np.random.uniform(5,60)
    #         listaPosiblesEventos.update({'FALTA':tiempoPerdido})
    #         probabilidad = np.random.randint(1,5)
    #         if probabilidad == 1:
    #             pass
    #             proxEvento = 'LESION'
    #         elif probabilidad == 4:
    #             proxEvento = 'PENAL'
    #         else:
    #             proxEvento = 'REANUDACION'            
    #     # Probabilidad de Penales
    #     if (pPenal <= penal):
    #         evento = 'PENAL'
    #         tiempoPerdido = np.random.uniform(45,240)
    #         listaPosiblesEventos.update({'PENAL':tiempoPerdido})
    #         probabilidad = np.random.randint(1,2)
    #         if probabilidad == 1:
    #             proxEvento = 'REANUDACION'
    #         else:
    #             proxEvento = 'GOL'            
    #     if (pLaterales <= laterales):
    #         evento = 'LATERAL'
    #         tiempoPerdido = np.random.uniform(5,45)
    #         listaPosiblesEventos.update({'LATERAL':tiempoPerdido})
    #         proxEvento = 'REANUDACION'
    #         #listaPosiblesEventos.append('LATERAL')
    #     if (pLesion <= lesion):
    #         evento = 'LESION'
    #         tiempoPerdido = np.random.uniform(60,240)
    #         listaPosiblesEventos.update({'LESION':tiempoPerdido})
    #         proxEvento = 'CAMBIO'
    #         #listaPosiblesEventos.append('LESION')            
    #     if len(listaPosiblesEventos) == 0:
    #         evento = 'NADA'
    #         tiempoPerdido = np.random.uniform(5,45)
    #         listaPosiblesEventos.update({'NADA':tiempoPerdido})
    #         #listaPosiblesEventos.append('NADA')
    #     evento = choice(tuple(listaPosiblesEventos.keys()))
        
    #     return evento, tiempoPerdido, proxEvento
    #     #return  elegido,listaPosiblesEventos[elegido]