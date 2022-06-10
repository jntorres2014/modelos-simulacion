class Fechas(object):
    def __init__(self):
        self.fecha = {}
        self.fecha2 = []
        self.tiempoEfectivoFecha = 0



    def obtenerEstadisticasDePartido(self,numeroPartido,partido):
        self.fecha.update({numeroPartido:partido})
        self.fecha2.append(partido)
        self.tiempoEfectivoFecha += partido.tiempoEfectivo
    
    
    def mostrarEstadisticasFecha(self):
        print("El tiempo efectivo por fecha: ",self.tiempoEfectivoFecha)


    def __str__(self):
        pass