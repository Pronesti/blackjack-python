#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:14:05 2019

@author: diego
"""

import random

def crear_mazo(nro):
    mazo=[]
    h= 0
    while h < nro:
        i = 0
        j = 1
        while i < 4:
            j=1
            while j <= 13:
                mazo.append(j)
                j+=1
            i+=1
        h+=1
    random.shuffle(mazo)
    return mazo

def sumar_cartas(mano):
    i=0
    suma=0
    while i < len(mano):
        if mano[i] > 10:
            suma += 10
        elif (mano[i] == 1) and (suma+10 <= 21):
            suma += 11
        else:
            suma += mano[i]
        i+=1
    return suma
        
def jugar(mazo):
    mano = []
    while sumar_cartas(mano) < 21:
        mano.append(mazo.pop())
        print("Mano:", mano)
    print("------")
    print("Total:", sumar_cartas(mano))
    print("")
    return sumar_cartas(mano)

def jugar_varios(mazo, cant_jugadores):
    i=0
    resultado=[]
    while i < cant_jugadores:
        print("Jugador", i, ":")
        resultado.append(jugar(mazo))
        i+=1
    return resultado

def ver_quien_gano(listaResultados):
    i=0
    ganador=0
    cuanto=0
    lista=[0] * len(listaResultados)
    while i < len(listaResultados):
        if listaResultados[i] > cuanto:
            ganador= i
            cuanto = listaResultados[i]
        i+=1
    lista[ganador]= 1
    return lista

def experimentar(repeticiones, jugadores):
    i=0
    resultado_final = []
    while i < repeticiones:
        print("Repeticion n°", i,":")
        print("-----")
        mazo = crear_mazo(round(jugadores/2))
        resultado_parcial = ver_quien_gano(jugar_varios(mazo, jugadores))
        resultado_final.append(resultado_parcial)
        i+=1
    return sumar_resultado_partidas(resultado_final)

def sumar_resultado_partidas(lista_resultados):
    i=0
    j=0
    
    cantidad_jugadores = len(lista_resultados[0])
    cantidad_repeticiones = len(lista_resultados)
    resultado_total = [0] * cantidad_jugadores
    final_string = [""] * cantidad_jugadores
    while j < cantidad_jugadores: # hace 5 que son la cant de jugadores
        i=0
        while i < cantidad_repeticiones: # hace 10 veces que repite
            resultado_total[j] += lista_resultados[i][j]
            i+=1
        final_string[j] = "Jugador {}: {} partidas ganadas".format(j,resultado_total[j]) 
        j+=1
    for x in final_string:
        print(x)
    #return final_string
#mazo = crear_mazo(1)
#jugar(mazo)
#res = ver_quien_gano(jugar_varios(mazo,3))
numero_de_jugadores=int(input("Ingrese el numero de jugadores: "))
numero_de_repeticiones=int(input("Ingrese la cantidad de repeticiones: "))
experimentar(numero_de_repeticiones, numero_de_jugadores)
