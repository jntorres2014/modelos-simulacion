
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
    #     # 'ARRIVO',
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
    #     # 'ARRIVO',
    #     # 'PARTIDA'
    #     # 'LESIONADO'
    #     # 'NADA',]

    #     eventosPosibles2 = [
    #         'INTERRUPCION',
    #         'ARRIVOS',
    #         'FNC' #FALTAS NO COBRADAS
    #     ]
    #     # #evento con probabilidad de ocurrencia
    #     # dicEventos = {
    #     #     'GOL': 0.5,
    #     #     'CAMBIO':0.3, 
    #     #     'FALTA':0.8,
    #     #     'LATERAL':0.75,
    #     #     'ARRIVO':0.60,
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




    # def obtenerEstadisticasDeTorneo(self):
    #     print("*************ESTADISTICAS DE TORNEO********")
    #     totalTiempoPerdidoFaltas = 0
    #     totalTiempoPerdidoCambios =0
    #     totalTiempoPerdidoLaterales =0
    #     totalTiempoPerdidoPenal=0
    #     totalTiempoPerdidoGol=0 
    #     totalTiempoPerdidoLesionados=0 
    #     totalTiempoPerdidoAforo=0 
    #     totalTiempoPerdidoEventoExterno=0  
    #     totalTiempoPerdidoNada=0 
    #     totalCantCambios=0 
    #     totalCantLaterales=0 
    #     totalCantPenal=0 
    #     totalCantGol=0 
    #     totalCantLesionados=0 
    #     totalCantAforo=0 
    #     totalCantEventoExterno=0  
    #     totalCantFaltas=0 
    #     totalCantNada=0   
    #     totalTiemposEfectivos= 0
    #     print(len(self.fechasTorneo))
    #     for fechas in self.fechasTorneo:    
    #         for tuplas in fechas.partidos:
    #             totalTiempoPerdidoFaltas += tuplas.tiempoPerdidoFaltas
    #             totalTiempoPerdidoCambios +=tuplas.tiempoPerdidoCambios
    #             totalTiempoPerdidoLaterales +=tuplas.tiempoPerdidoLaterales
    #             totalTiempoPerdidoPenal+=tuplas.tiempoPerdidoPenal
    #             totalTiempoPerdidoGol+=tuplas.tiempoPerdidoGol 
    #             totalTiempoPerdidoLesionados+=tuplas.tiempoPerdidoLesionados 
    #             totalTiempoPerdidoAforo+=tuplas.tiempoPerdidoAforo 
    #             totalTiempoPerdidoEventoExterno+=tuplas.tiempoPerdidoEventoExterno  
    #             totalTiempoPerdidoNada+=tuplas.tiempoPerdidoNada 
    #             totalCantCambios+=tuplas.cantCambios 
    #             totalCantLaterales+=tuplas.cantLaterales 
    #             totalCantPenal+=tuplas.cantPenal 
    #             totalCantGol+=tuplas.cantGol 
    #             totalCantLesionados+=tuplas.cantLesionados 
    #             totalCantAforo+=tuplas.cantAforo 
    #             totalCantEventoExterno+=tuplas.cantEventoExterno  
    #             totalCantFaltas+=tuplas.cantFaltas 
    #             totalCantNada+=tuplas.cantNada
    #             totalTiemposEfectivos += tuplas.tiempoEfectivo

    #             print("*************PARTIDOS***************")
    #             totalTiempoPerdidoFaltas = totalTiempoPerdidoFaltas / self.cantidadPartidos
    #             totalTiempoPerdidoCambios = totalTiempoPerdidoCambios /self.cantidadPartidos
    #             totalTiempoPerdidoLaterales = totalTiempoPerdidoLaterales/self.cantidadPartidos
    #             totalTiempoPerdidoPenal=totalTiempoPerdidoPenal /self.cantidadPartidos
    #             totalTiempoPerdidoGol=  totalTiempoPerdidoGol/self.cantidadPartidos
    #             totalTiempoPerdidoLesionados= totalTiempoPerdidoLesionados/self.cantidadPartidos
    #             totalTiempoPerdidoAforo= totalTiempoPerdidoAforo/self.cantidadPartidos
    #             totalTiempoPerdidoEventoExterno= totalTiempoPerdidoEventoExterno/self.cantidadPartidos  
    #             totalTiempoPerdidoNada= totalTiempoPerdidoNada/self.cantidadPartidos

    #             totalCantCambios=  totalCantCambios/self.cantidadPartidos
    #             totalCantLaterales=  totalCantLaterales/self.cantidadPartidos
    #             totalCantPenal=  totalCantPenal/self.cantidadPartidos
    #             totalCantGol=totalCantGol /self.cantidadPartidos
    #             totalCantLesionados= totalCantLesionados/self.cantidadPartidos
    #             totalCantAforo=  totalCantAforo/self.cantidadPartidos
    #             totalCantEventoExterno=  totalCantEventoExterno /self.cantidadPartidos
    #             totalCantFaltas= totalCantFaltas /self.cantidadPartidos
    #             totalCantNada= totalCantNada /self.cantidadPartidos
    #             totalTiemposEfectivos =  totalTiemposEfectivos/self.cantidadPartidos

    #         print ("cantidad de partidos: ",self.cantidadPartidos)
    #         print("CANTIDADES")
    #         print(("Faltas: {0}\nCambios: {1}\nLaterales: {2}\nPenales: {3}\nGOL: {4}\nLESION: {5}\nAFORO: {6}\nEVENTO EXTERNO: {7}\nNADA: {8}\n".format(
    #         totalCantFaltas, 
    #         totalCantCambios, 
    #         totalCantLaterales, 
    #         totalCantPenal, 
    #         totalCantGol, 
    #         totalCantLesionados, 
    #         totalCantAforo,
    #         totalCantEventoExterno,  
    #         totalCantNada,   
    #         )))
    #         print("TIEMPOS PERDIDOS")
    #         print("Faltas: {0}\nCambios: {1}\nLaterales: {2}\nPenales: {3}\nGOL: {4}\nLESION: {5}\nAFORO: {6}\nEVENTO EXTERNO: {7}\nNADA: {8}\nTotal TiemposEfectivos: {9}".format(
    #         totalTiempoPerdidoFaltas,
    #         totalTiempoPerdidoCambios,
    #         totalTiempoPerdidoLaterales,
    #         totalTiempoPerdidoPenal,
    #         totalTiempoPerdidoGol, 
    #         totalTiempoPerdidoLesionados, 
    #         totalTiempoPerdidoAforo, 
    #         totalTiempoPerdidoEventoExterno,  
    #         totalTiempoPerdidoNada,
    #         totalTiemposEfectivos))

    #
    #     def exportarEstadisticas(self):
        # fechas=self.fechasTorneo
        # fechas2 = self.fechas
        # partidos = []
        # arrFecha = {}
        # n=0
        # print("fechas: ",fechas2.keys())
        # for fecha in fechas:
        #     n+=1
        #     print("fechas {0} {1}\n".format(n,fechas))

        # data = pd.DataFrame(data= np.array(fechas2.keys()))

        # #dicFechas = self.fechas
        # print(type(fechas2))
        # for fecha in fechas:
        #     arrFecha.update(fecha)
        #     for partido in fecha.partidos:
        #         print(type(partido))
        #         partidos.append(partido)

                #print(partido)
    
	
    #     classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
    #        'Data Sciece','others']
    #     class1_students = [45, 15, 35, 25, 30]
    #     print(self.tiempoEfectivoTorneo)
    #     #data = pd.DataFrame(classes)
    #     #print (data)
    #     datos= []
    #     #data.to_excel('sample_data.xlsx', sheet_name='sheet1')
    #     colores = ['red','green','blue','yellow','orange','black','violet','lightblue','pink']
    #     plt.pie(self.tiempoEfectivoTorneo)
    #     #plt.pie(1)
    #     plt.savefig("./static/tiemposPerdidos2.png") 
    #     plt.show() 
    #     return 
    # # #
        #print("Evento: ",evento)
        # if (evento=='GOL'):
        #     self.cantGol += 1
        #     self.tiempoPerdidoGol += tiempo
        # if cantidadDeCambios < 6:    
        #     if (evento=='CAMBIO'):
        #         self.cantCambios +=1
        #         self.tiempoPerdidoCambios += tiempo
        # if (evento=='LATERAL'):
        #     self.cantLaterales +=1  
        #     self.tiempoPerdidoLaterales += tiempo
        # if (evento=='PENAL'):
        #     self.cantPenal += 1
        #     self.tiempoPerdidoPenal += tiempo
        # if (evento=='LESION'):
        #     self.cantLesionados +=1
        #     self.tiempoPerdidoLesionados += tiempo
        # if (evento=='AFORO'):
        #     self.cantAforo +=1
        #     self.tiempoPerdidoAforo += tiempo
        # if (evento=='EVENTOEXTERNO'):
        #     self.cantEventoExterno += 1 
        #     self.tiempoPerdidoEventoExterno += tiempo           
        # if (evento=='FALTA'):
        #     self.cantFaltas +=1
        #     self.tiempoPerdidoFaltas += tiempo
        # if (evento=='NADA'):
        #     self.cantNada +=1
        #     self.tiempoPerdidoNada += tiempo

# ranges = {
#     'GOL': (0.,.004),
#     'CAMBIO': (.04, 0.12),
#     'LESION': (.120,0.0160),
#     'LATERAL': (0.190,0.210),
#     #'INTERRUPCION': (0.260,0.330),
#     #'falta_amonestacion_tiroLibre': (0.330 ,0.380),
#     'FALTA':(0.330 ,0.340),
#     #'PENAL': ('dependeraDeFalta'), 
#     'EVENTOEXTERNO': (0.380, 0.388),
#     'EVENTOEXTERNO': (0.388,0.391),
#     'NADA': (.12, 1.)
# }
