class Fechas(object):
    def __init__(self):
        self.fecha = {}
        self.partidos = []
        self.tiempoEfectivoFecha = 0
        self.tiemposPerdidos= self.inicializar_contadores()
        self.cantidadInterrupciones = self.inicializar_contadores()
    
    def inicializar_contadores(self):
        return {
            'FALTA': 0,
            'CAMBIO': 0,
            'LATERAL': 0,
            'PENAL': 0,
            'GOL': 0,
            'LESION': 0,
            'AFORO': 0,
            'AFORO': 0,
            'EVENTOEXTERNO': 0,
            'TIRO_DE_ESQUINA': 0,
            'NADA': 0
        }    

    def obtenerEstadisticasDePartido(self,numeroPartido,partido):
        self.fecha.update({numeroPartido:partido})
        self.partidos.append(partido)
        self.tiempoEfectivoFecha += partido.tiempoEfectivo
        type(partido.tiemposPerdidos)
        print("********FECHAAA************")
        for eventos,tiempos in partido.tiemposPerdidos.items():
            self.tiemposPerdidos[eventos] += tiempos

        for eventos,tiempos in partido.cantidadInterrupciones.items():
            self.cantidadInterrupciones[eventos] += tiempos
        

    def mostrarEstadisticasFecha(self):
        print("*******FECHAS*********")
        print("El tiempo efectivo por fecha: ",self.tiempoEfectivoFecha)
        print("**************************")
    


    def __str__(self):
        return "tiempos peridos: {0}\ncantidades Perdidas{1}".format(self.tiemposPerdidos,self.cantidadInterrupciones)