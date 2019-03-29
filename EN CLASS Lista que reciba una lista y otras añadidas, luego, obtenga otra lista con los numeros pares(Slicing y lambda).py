"""

Hacer una funcion que reciba una lista con listas añiadidas y obtenga
otra con los números pares.Use slicing y lambda en classe

"""
class ParesPares(object):
    def __int__(self,lista):
        pass
    def listas_par(self, lista):
        cond =lambda lista :lista%2 == 0
        if isinstance (lista, list):
            return self.list_par_aux(lista, cond, [])
        else: return "Parametro no funciona"

    def list_par_aux(self, lista,cond, resultado):
        if lista ==[]:
            return resultado
        elif isinstance (lista[0], list):
            return self.list_par_aux(lista[0] + lista[1:], cond, resultado)
        elif cond(lista[0]):
            return self.list_par_aux(lista[1:], cond, resultado + [lista[0]])
        else: return self.list_par_aux(lista[1:], cond, resultado)
