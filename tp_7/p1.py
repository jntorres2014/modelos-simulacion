# Se desea determinar el tiempo promedio que los camiones deben esperar en las colas de carga, 
# expresando tal medida mediante un intervalo de confianza cuyo nivel de confiabilidad sea 95%, 
# simulando al menos 60 experimentos de 100 corridas cada uno.

from ast import ClassDef
from ctypes import cast
from math import log
from pydoc import classify_class_attrs, classname
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

EXP = 60
CORR= 100

class EventoCamiones():
    def __init__(self, tiempoLlegada):
        self.tiempoLlegada = tiempoLlegada
        

        
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

tiempo_de_carga = 0

for corr in range(CORR):
    for exp in range(EXP):
        arriboCamion= np.random.exponential(15)
        surtido_uno = np.random.normal(18, 4)
        surtido_dos = np.random.exponential(15)
        surtidor_tres= np.random.exponential(16)
        surtido_cuatro = np.random.normal(14, 3)
        tiempo_de_carga = tiempo_de_carga + arriboCamion

print("arribo Camiones: ",arriboCamion)
print("surtidor uno: ", surtido_uno)
print("surtidor dos: ", surtido_dos)
print("surtidor tres: ", surtidor_tres)
print("surtidor cuatro: ", surtido_cuatro)
promedio = tiempo_de_carga / (CORR * EXP)
print("promedio", promedio)
