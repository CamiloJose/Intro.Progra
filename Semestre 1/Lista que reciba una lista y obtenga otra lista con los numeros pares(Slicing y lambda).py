#Hacer una lista que reciba una lista y obtenga otra lista con los numeros pares.
#Utilice slicing y funciones lambda

#============================================================


def listas_con_par(lista):
    cond =lambda lista :lista%2 == 0
    if isinstance (lista, list):
        return listas_par_aux(lista, cond, [])
    else: return "AAAHHHHHHH"

def listas_par_aux(lista,cond, resultado):
    if lista ==[]:
        return resultado
    elif cond(lista[0]):
        return listas_par_aux(lista[1:], cond, resultado + [lista[0]])
    else: return listas_par_aux(lista[1:], cond, resultado)

