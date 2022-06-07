from cgi import print_environ
from random import random, sample
import random
import numpy as np
PORCENTAJE= 0.45

class Estadio(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.capacidad= random.randint(300,1000)
        self.capacidadMinima = int(self.capacidad * PORCENTAJE)
        self.cantidadAcceso= random.randint(1,3)
    
    def cumpleAforo(self, cantidadHinchas):
        return (self.capacidadMinima <= cantidadHinchas)
    
    def __str__(self):
        return "Estadio: %s Capacidad: %s Capacidad Minima: %s Cantidad de Accesos: %s" % (self.nombre, self.capacidad,self.capacidadMinima, self.cantidadAcceso)
    