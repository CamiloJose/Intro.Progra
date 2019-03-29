"""
Hacer una lista que reciba una lista y obtenga otra lista con los numeros pares.
    Utilice slicing
    funciones lambda
    clases
#============================================================
"""


class lista_Par(object):
    def __int__(self,lista):
        pass
    def listas_con_par(self, lista):
        cond =lambda lista :lista%2 == 0
        if isinstance (lista, list):
            return self.listas_par_aux(lista, cond, [])
        else: return "AAAHHHHHHH"

    def listas_par_aux(self, lista,cond, resultado):
        if lista ==[]:
            return resultado
        elif cond(lista[0]):
            return self.listas_par_aux(lista[1:], cond, resultado + [lista[0]])
        else: return self.listas_par_aux(lista[1:], cond, resultado)

"""
Para poner en Shell

su = lista_Par()
su.listas_con_Par([1,2,3,4,5,66,7,8,9])

"""

# proff

class Par(object):
    def __init__(self):
        pass
    def pares(self, lista):
        condicion = lambda numero : numero % 2 == 0
        if isinstance(lista, list) and lista !=[]:
            return self.pares_aux(lista, condicion, [])
        else:
            return "Error"
    def pares_aux(self, lista, condicion, resultado):
        if lista == []:
            return resultado
        elif condicion (lista[0]):
            return ((self.pares_aux(lista[1:], condicion, [lista[0]] + resultado)))
        else:
            return self.pares_aux(lista[1:], condicion, resultado)
                                
