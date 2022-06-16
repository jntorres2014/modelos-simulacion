def evento_en_rango(num):
    rangos = {
        'CAMBIO': (0., .0307),
        'GOL': (.0307, .031),
        'LESION': (.031, .0312),
        'LATERAL': (.0312, .033),
        'TIRO_DE_ESQUINA': (.033, .034),
        'FALTA': (.034, .0355),
        'EVENTOEXTERNO': (.0355, .0356),
        'NADA': (.0356, 1.)
    }

    for evento, rng in rangos.items():
        if rng[0] == 0.:
            if rng[0] <= num <= rng[1]:
                return evento
        elif rng[0] < num <= rng[1]:
            return evento


def generar_fel(numeros):
    return [evento_en_rango(num) for num in numeros]