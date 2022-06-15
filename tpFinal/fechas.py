class Fechas(object):
    def __init__(self):
        self.fecha = {}
        self.partidos = []
        self.tiempoEfectivoFecha = 0
        self.tiemposPerdidos= {}
        self.cantidadIterrupciones = {}
    

    def obtenerEstadisticasDePartido(self,numeroPartido,partido):
        self.fecha.update({numeroPartido:partido})
        self.partidos.append(partido)
        self.tiempoEfectivoFecha += partido.tiempoEfectivo
        self.tiemposPerdidos[numeroPartido] = [partido.tiemposPerdidos,partido.cantidadInterrupciones]
        

    def mostrarEstadisticasFecha(self):
        print("**************************")
        print("El tiempo efectivo por fecha: ",self.tiempoEfectivoFecha)
        print("**************************")
    


    def __str__(self):
        pass