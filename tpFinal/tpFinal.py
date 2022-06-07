from ast import If
from socket import if_nameindex
from time import sleep, time
import matplotlib.pyplot as plt
import numpy as np

EXP = 30
COR = 100


#------------------Considereaciones-----------------#
# Capacidades de cada estadio: Generar un número aleatorio (entero) entre 300 y 1000 para determinar la cantidad de asientos de cada estadio. 
# Para cada uno, asuma una proporción de 50% de espectadores locales y visitantes.
# Determinar la ocurrencia de un evento de interrupción: 
# Utilice la tabla de distribución correspondiente. 
# Los valores de la columna “Probabilidad de ocurrencia” servirán como umbral. 
# Genere un número aleatorio (real) entre 0.0 y 1.0, si númerogenerado <= umbral, el evento ocurre. 
# Asuma una distribución de 50% para determinar si beneficia al equipo local o visitante.
# Determinar si un espectador se retira: Una vez que ocurre uno de los eventos determinados y si corresponde, 
# generar un número aleatorio (real) entre 0.0 y 1.0. 
# Si númerogenerado <= 0.005, el espectador se retira. 
# Caso contrario, el evento de retiro no ocurre.

def inicializador():
    capacidadEstadio = np.random.randint(300,1000)
    aforoPublico = capacidadEstadio * 0.45

    hinchasLocales= capacidadEstadio // 2
    retirandoGente = np.random.uniform(0.0,1.0)
    cont = 0
    tiempoPerdido = 0
    cantGoles = 0
    cantFaltas = 0
    cantCambios = 0
    cantPenal = 0
    cantLesion = 0
    cantIngresoHincha = 0
    cantLaterales = 0
    laterales = 0.2
    cambio= 0.07
    lesion =0.03
    penal =0.02
    ingresoHincha= 0.008 
    perro = 0.003
    falta = 0.2
    gol = 0.04
    
    while (cont<90):
        #sleep(1)
        pgol =np.random.uniform(0.0,1.0)
        pCambio = np.random.uniform(0.0,1.0) 
        pFalta= np.random.uniform(0.0,1.0)
        pPenal = np.random.uniform(0.0,1.0)
        pLaterales = np.random.uniform(0.0,1.0)
        pLesion = np.random.uniform(0.0,1.0)
        # Probabilidad de Gol

        if (pgol <= gol):
            #gol equipo local
            #hinchas visitantes se van  
            tiempo = np.random.uniform(10,60)
            tiempoPerdido =  tiempoPerdido + tiempo
            print("Gol! ", cont, f"{tiempo:.2f}")
            cantGoles = cantGoles +1
        # Probabilidad de Cambios
        if (pCambio <= cambio)and(cantCambios < 6):
            tiempo = np.random.uniform(10,45)
            tiempoPerdido =  tiempoPerdido + tiempo
            print("Cambio! ", cont, f"{tiempo:.2f}")
            cantCambios = cantCambios +1
        # Probabilidad de Faltas cometidas
        if (pFalta <= falta):
            tiempo = np.random.uniform(5,60)
            tiempoPerdido =  tiempoPerdido + tiempo
            print("Falta! ", cont, f"{tiempo:.2f}")
            cantFaltas = cantFaltas +1
        # Probabilidad de Penales
        if (pPenal <= penal):
            tiempo = np.random.uniform(45,240)
            tiempoPerdido =  tiempoPerdido + tiempo
            print("Penal para boca! ", cont, f"{tiempo:.2f}")
            cantPenal = cantPenal +1
        if (pLaterales <= laterales):
            tiempo = np.random.uniform(5,45)
            tiempoPerdido =  tiempoPerdido + tiempo
            print("Lateral! ", cont, f"{tiempo:.2f}")
            cantLaterales = cantLaterales +1
        if (pLesion <= lesion):
            tiempo = np.random.uniform(60,240)
            tiempoPerdido =  tiempoPerdido + tiempo
            print("Lesion ! ", cont, f"{tiempo:.2f}")
            cantLesion = cantLesion +1
        # if (pHinchas <= ):
        #     tiempo = np.random.uniform(60,240)
        #     tiempoPerdido =  tiempoPerdido + tiempo
        #     print("Lesion ! ", cont, f"{tiempo:.2f}")
        #     cantLesion = cantLesion +1
        
        cont = cont+1

            
    print("Aforo de publico", aforoPublico)
    print("cantidad de goles: ", cantGoles)
    print("cantidad de cambios: ", cantCambios)
    print("cantidad de faltas: ", cantFaltas)
    print("cantidad de penales: ", cantPenal)
    print("cantidad de Lesiones: ", cantLesion)
    print("cantidad de Laterales: ", cantLaterales)    

    print("tiempo perdido: ",f"{tiempoPerdido:.2f}", tiempoPerdido/ 60)
