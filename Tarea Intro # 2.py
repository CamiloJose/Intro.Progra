#Introducción
#ESTA FUCNION *NO* ES CORRECTA
import math
class Medias:
    def __init__(self):
        pass
    def MediaGeo(self,lista):
        if  isinstance (lista,list) and len(lista)>0:
            return self.Media(lista)**(1/len(lista), self.Media(lista))
        else:
            return "Error la lista no es lo suficientemente grande"
    def Media(self,lista):
        if lista==[]:
            return []
        else:
            return lista[0]* self.Media(lista[1:])


#FUCNION CORRECTA

def mediageometrica(lista):
    if isinstance(lista,list):
        return medicion_aux(lista), medicion_2(lista)
    else:return"Error no ingrerso los valores necesarios"

def medicion_aux(lista):
    if lista == [ ]:
        return 1
    if lista[0] > 0:
        return (lista[0] * medicion_aux(lista[1:]))

def medicion_2(lista):
    if lista == [ ] :
        return 1
    else:
        return (lista[0] * medicion_aux(lista[1:])) ** (1/ len(lista)) -1
