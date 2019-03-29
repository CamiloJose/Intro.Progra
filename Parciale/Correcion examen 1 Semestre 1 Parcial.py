"""
Proffesor solucion del examen

"""
#   Ejercicio 1
def combinaciones(hp, dell):
    if (isinstance(hp, list) and isinstance(dell, list) and len(hp) >0 and len(dell) >0):
        return combinaciones_aux(hp, dell, [])
    else: return "Los parametros no son admitidos"

def combinaciones_aux(hp, dell, resultado):
    if hp == []:
        return resultado
    else: return combinaciones_aux(hp[1:],dell,resultado + comb_aux(hp[0], dell, []))

def comb_aux(valor, dell, result):
    if dell == []:
        return result
    else: return comb_aux(valor, dell[1:], result + [valor + dell[0]])

#   Ejercicio 2

import math
def std(lista,avg):
    if(isinstance(lista, list) and isinstance(avg, float)):
        return math.sqrt(std_aux(lista, avg) /(len(lista) - 1))
    else: return "Error"

def std_aux(lista, avg):
    if lista == []:
        return 0
    else: return ((lista[0] - avg) ** 2) + std_aux(lista[1:], abg)

#   Ejercicio 3

def zScore(listaX, S, avg):
    if (isinstance(listaX, list) and type(avg)==float and type(s)==float):
        return zScore_aux(listaX, avg, S)
    else: return "Los parametros no son listas o están vacias"

def zScore_aux(listaX, avg, s):
    if lista ==[]:
        return []
    else: retrun [(lista[0] - avg)/ s]+ zScore_aux(lista[1:], avg, s)

#   Ejercicio 4

def rScore(Sx, Sy):
    if(isinstance(Sx, list) and isinstance(Sy, list) and len(Sx) ==len (Sy)):
       return rScore_aux(Sx, Sy) / (len(Sx) - 1)
    else: return "Los parametros no son listas o estan vacias"

def rScore_aux(Sx, Sy):
    if Sx == []:
        return 0
    else: return (Sx[0] * Sy[0]) + rScore_aux(Sx[1:], Sy [1:])
