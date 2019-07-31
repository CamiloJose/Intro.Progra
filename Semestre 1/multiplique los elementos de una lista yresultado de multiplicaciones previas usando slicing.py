#Recurcion de cola
#Hacer una fucnion que multiplique los elementos de una lista
#por el resultado de multiplicaciones previas usando slicing
def multiplicacion(lista):
    if isinstance(lista, list):
        return multiplicacion_aux(lista,1)
    else:
        return "Error: el numero no es lista"
def multiplicacion_aux(lista, resultado):
    if lista == []:
        return resultado
    else:
        return multiplicacion_aux(lista[1:], resultado*lista[0])

#=============================================================================================

#Proffe

def lista1(lista):
    if isinstance(lista, list) and lista !=[]:
        return lista1_aux(lista, 1)
    else:
        return "Erroe"

def lista1_aux(lista, resultado):
    if lista == []:
        return resultado
    else:
        return lista1_aux(lista[1:], resultado * lista[0])
