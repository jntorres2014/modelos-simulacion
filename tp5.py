#!/usr/bin/env python
# coding: utf-8
import numpy as np

EXP = 30
COR = 100

def confidence_interval(n_sample, mean, std):
    # By default, it calculates the CI with a confidence level of 99%
    # Change `z_value` accordingly.
    # Optionally, use `coeff` to get a CI with a greater error margin
    z_value=2.57
    coeff=1.0
    z_term = coeff * (z_value * std / (n_sample ** 0.5))
    inf = mean - z_term
    print("zterm",z_term)
    print("inf",inf)
    sup = mean + z_term
    print("sup ",sup)
    return inf, sup

def porcentajeCritico (tiempo, tiempo_total):
    return  (tiempo * 100 / tiempo_total)


criticidades = {'sup': 0, 'medio': 0, 'inf': 0}
tiempos_ejecucion_exp = []
for exp in range(EXP):
    tiempos_ejecucion_corr = []
    for cor in range(COR):
        # generar numeros aleatorios para cada tarea
        a = np.random.uniform(2,4)
        b = np.random.uniform(3,6)
        c = np.random.uniform(2,5)
        d = np.random.uniform(3,6)
        e = np.random.uniform(2,5)
        f = np.random.uniform(4,8)
        g = np.random.uniform(3,7)

        tiempo_total = a + b + c + d + e + f + g # en minutos
        
        #   Tiempo superior
        tiempo_sup = a + b + c
        #crit_sup = tiempo_sup * 100 / tiempo_total
        criticidades['sup'] = porcentajeCritico(tiempo_sup, tiempo_total)
        
        #   Tiempo Medio
        tiempo_medio = d + e 
        criticidades['medio'] = porcentajeCritico(tiempo_medio, tiempo_total)
        
        #   Tiemp
        
        tiempo_inf = f + g 
        
        criticidades['inf'] = porcentajeCritico(tiempo_inf, tiempo_total)
        
        tiempos_ejecucion_corr.append(tiempo_total)

    tiempos_ejecucion_exp.append(np.mean(tiempos_ejecucion_corr))
    print(tiempos_ejecucion_exp, "\n")
media= np.mean(tiempos_ejecucion_exp)
standar = np.std(tiempos_ejecucion_exp)
print("Media: ", media)
print("Desvio: ", standar)
ic = confidence_interval(100, media,standar)
print("Intervalo de confianza: ", ic)


